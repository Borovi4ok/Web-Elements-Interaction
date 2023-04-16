import inspect
import pytest
import random
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.data.test_data import TestData
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions


# Suite 5. Test Web Tables
class TestWebTable(Assertions, ReusableFunctions):
    @pytest.mark.webtables
    def test_url_webtable(self, urls):
        self.driver.get(urls["webtables"])
        self.verify_url("webtables")

    @pytest.mark.webtables
    def test_webtable_header_sorted(self):
        # click each column header and verify if sorted

        headers_list = self.driver.find_elements(By.CLASS_NAME, "rt-resizable-header-content")
        num_columns = 6
        # number of testable (sortable) columns in table
        for i in range(0, num_columns):
            headers_list[i].click()
            # a column should be sorted

            ind = i + 1
            # 'ind' = index for a column selector, (in DOM row (class='rt-td') number in order)
            items_list = self.get_column_data(ind, as_int=True)
            # 1 (True) to get digits as "int" to verify alphabetically

            sorted_items = sorted(items_list)
            self.verify_equal(items_list, sorted_items)

    @pytest.mark.webtables
    def test_webtable_search_field(self):
        # pick any value from each column and search in table

        num_columns = 6
        # number of testable (searchable) columns in table

        for ind in range(1, num_columns + 1):
            # 'ind' = index for a column selector, (in DOM row (class='rt-td') number in order)

            items_list = self.get_column_data(ind, as_int=False)
            # call reusable func to get data from a column before search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            rand_ind = random.randrange(0, len(items_list))

            search_value = items_list[rand_ind]
            self.driver.find_element(By.ID, "searchBox").send_keys(search_value)
            # insert any value from given column to 'search' box

            search_result_list = self.get_column_data(ind, as_int=False)
            # call reusable func to get data from a column after search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            for result in search_result_list:
                self.verify_in_text(search_value, result)
                self.driver.refresh()
                # refresh since original rows of the table are not being displayed after clearing the search box
                # send_keys(Keys.RETURN) or clicking on another element on the page after clearing search - not helpful

    @pytest.mark.webtables
    def test_webtable_add_row(self):
        # Add a row with test data

        rows_list = self.get_column_data(1, as_int=False)
        original_rows_amount = len(rows_list)
        # take a list of rows in first column and define an original number of filled rows

        self.driver.find_element(By.ID, "addNewRecordButton").click()

        registration_form_fields = self.driver.find_elements(By.CSS_SELECTOR, ".mr-sm-2.form-control")
        # list of fields in edit form

        range_max = len(registration_form_fields)

        self.clear_and_fill_in(0, range_max, registration_form_fields, TestData.data_add_row_table)

        self.driver.find_element(By.ID, "submit").click()
        # click "Submit" button

        elements_list = self.driver.find_elements(By.XPATH,
                                                  f"(//div[@class='rt-tr -odd' or @class='rt-tr -even'])[{original_rows_amount + 1}]/div")
        # list of all added elements in the new row

        elements_list.pop()
        # delete the last element with 'Edit" button

        added_data = self.extract_text_from_list(elements_list)
        # extract text

        self.verify_equal(added_data.sort(), TestData.data_add_row_table.sort())
        # verify data from added row is equal to sent test-data
        # sort() both first, because order of elements in a row and in 'Registration form" (add form) is not the same

    @pytest.mark.webtables
    def test_webtable_edit_row(self):
        # Edit previously created row with test data
        self.driver.find_element(By.XPATH,
                                 f"//div[@class='rt-td' and text()='{TestData.data_add_row_table[1]}']/following-sibling::div//span[@title='Edit']").click()
        # click edit button for the row with test data

        registration_form_fields = self.driver.find_elements(By.CSS_SELECTOR, ".mr-sm-2.form-control")
        # list of fields in edit form

        range_max = len(registration_form_fields)

        self.clear_and_fill_in(0, range_max, registration_form_fields, TestData.data_edit_row_table)

        self.driver.find_element(By.ID, "submit").click()
        # click "Submit" button

        elements_list = self.driver.find_elements(By.XPATH,
                                                  f"//div[@class='rt-td' and text()='{TestData.data_edit_row_table[1]}']/following-sibling::div//span[@title='Edit']")
        # list of all edited elements in the edited row

        elements_list.pop()
        # delete the last element with 'Edit" button

        edited_data = self.extract_text_from_list(elements_list)
        # extract text

        self.verify_equal(edited_data.sort(), TestData.data_edit_row_table.sort())
        # verify data from edited row is equal to sent test-data
        # sort() both first, because order of elements in a row and in 'Registration form" (edit form) is not the same

    @pytest.mark.webtables
    def test_webtable_delete_row(self):
        # Delete a row with test data added previously

        log = Assertions.get_logger()
        test_func_name = inspect.stack()[1][3]

        first_column_elements = self.get_column_data(1, as_int=False)
        original_rows_amount = len(first_column_elements)
        # take a list of elements in the first column and define an original number of filled rows

        self.driver.find_element(By.XPATH,
                                 f"//div[@class='rt-td' and text()='{TestData.data_edit_row_table[1]}']/following-sibling::div//span[@title='Delete']").click()
        # delete

        verify_first_column_elements = self.get_column_data(1, as_int=False)
        left_rows_amount = len(verify_first_column_elements)
        self.verify_equal(left_rows_amount + 1, original_rows_amount)
        # verify number of columns one less

        path = f"//div[@class='rt-td' and text()='{TestData.data_edit_row_table[1]}']"
        self.verify_deleted(By.XPATH, path)
        # verify row with test data doesn't present in the table
