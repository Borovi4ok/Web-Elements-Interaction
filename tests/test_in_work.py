import random
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from WebInteractionDemoQA.test_data.data_test_elements import DataElements
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestElementsPage(Assertions, ReusableFunctions):
    # Suite 5. Test Web Tables
    @pytest.mark.webtables
    def test_url_element(self, urls):
        self.driver.get(urls["webtables"])
        self.verify_url("webtables")

    @pytest.mark.webtables
    def test_header_sorted(self):
        # click each column header and verify if sorted

        headers_list = self.driver.find_elements(By.CLASS_NAME, "rt-resizable-header-content")
        num_columns = 6
        # number of testable (sortable) columns in table
        for i in range(0, num_columns):
            headers_list[i].click()
            # a column should be sorted

            ind = i + 1
            # 'ind' = index for a column selector, (in DOM row (class='rt-td') number in order)
            items_list = self.get_column_data(ind, 1)
            # 1 (True) to get digits as "int" to verify alphabetically

            sorted_items = sorted(items_list)
            self.verify_equal(items_list, sorted_items)

    @pytest.mark.webtables
    def test_search_field(self):
        # pick any value from each column and search in table

        num_columns = 6
        # number of testable (searchable) columns in table

        for ind in range(1, num_columns + 1):
            # 'ind' = index for a column selector, (in DOM row (class='rt-td') number in order)

            items_list = self.get_column_data(ind, 0)
            # call reusable func to get data from a column before search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            rand_ind = random.randrange(0, len(items_list))

            search_value = items_list[rand_ind]
            self.driver.find_element(By.ID, "searchBox").send_keys(search_value)
            # insert any value from given column to 'search' box

            search_result_list = self.get_column_data(ind, 0)
            # call reusable func to get data from a column after search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            for result in search_result_list:
                self.verify_in_text(search_value, result)
                self.driver.refresh()
                # refresh since original rows of the table are not being displayed after clearing the search box
                # send_keys(Keys.RETURN) or clicking on another element on the page after clearing search - not helpful















    """# Suite 5. Test Web Tables
    @pytest.mark.webtables
    def test_url_element(self, urls):
        self.driver.get(urls["webtables"])
        self.verify_url("webtables")

    @pytest.mark.webtables
    def test_search_field(self):
        # pick any value from each column and search in table

        num_columns = 6
        # number of testable (searchable) columns in table

        for ind in range(1, num_columns + 1):
            # 'ind' = index for a column selector, (in DOM row (class='rt-td') number in order)

            items_list = self.get_column_data(ind, 0)
            # call reusable func to get data from a column before search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            rand_ind = random.randrange(0, len(items_list))

            search_value = items_list[rand_ind]
            self.driver.find_element(By.ID, "searchBox").send_keys(search_value)
            # insert any value from given column to 'search' box

            search_result_list = self.get_column_data(ind, 0)
            # call reusable func to get data from a column after search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            for result in search_result_list:
                self.verify_in_text(search_value, result)
                self.driver.refresh()
                # refresh since original rows of the table are not being displayed after clearing the search box
                # send_keys(Keys.RETURN) or clicking on another element on the page after clearing search - not helpful"""

    """@pytest.mark.webtables
    def test_data_edit(self):
        # pick any value from each column and replace with a test value

        num_columns = 6
        # number of testable (searchable) columns in table

        for ind in range(1, num_columns + 1):
            # 'ind' = index for a column selector, (in DOM row (class='rt-td') number in order)

            items_list = self.get_column_data(ind, 0)
            # call reusable func to get data from a column before search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            rand_ind = random.randrange(0, len(items_list))

            search_value = items_list[rand_ind]
            self.driver.find_element(By.ID, "searchBox").send_keys(search_value)
            # insert any value from given column to 'search' box

            search_result_list = self.get_column_data(ind, 0)
            # call reusable func to get data from a column after search
            # 0 parameter (False) to get digits as "str" to use verify_in_text assertion

            for result in search_result_list:
                self.verify_in_text(search_value, result)
                self.driver.refresh()
                # refresh since original rows of the table are not being displayed after clearing the search box
                # send_keys(Keys.RETURN) or clicking on another element on the page after clearing search - not helpful"""
