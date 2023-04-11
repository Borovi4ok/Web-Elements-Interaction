import pytest
import random
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.common.exceptions import NoSuchElementException


class TestElementsPage(Assertions, ReusableFunctions):
    # subclass with test functions for all elements in "Elements" section

    # Suite 1. Test blocks and text presence on "Elements" page
    @pytest.mark.elements
    def test_url_element(self, urls):
        self.driver.get(urls["elements"])
        self.verify_url("element")
        # to assert, verify_url method in use_fixtures

    @pytest.mark.elements
    def test_header_text(self):
        actual = self.driver.find_element(By.CLASS_NAME, "main-header").text
        self.verify_equal(actual, "Elements")

    @pytest.mark.elements
    def test_main_menu_presence(self):
        element = self.driver.find_element(By.CLASS_NAME, "left-pannel")
        self.verify_is_displayed(element)

    @pytest.mark.elements
    def test_select_message(self):
        actual = self.driver.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']").text
        self.verify_equal(actual, "Please select an item from left to start practice.")

    @pytest.mark.elements
    def test_footer_text(self):
        full_text = self.driver.find_element(By.CSS_SELECTOR, "footer span").text
        self.verify_in_text("ALL RIGHTS RESERVED", full_text)

    # Suite 2. Test text-box submit form on "text_box" page
    @pytest.mark.text_box
    def test_url_box(self, urls):
        self.driver.get(urls["text_box"])
        self.verify_url("text-box")

    @pytest.mark.text_box
    def test_submission_form(self):
        # invoke data-list set from test_data package
        data = DataElements.data_text_box

        self.driver.find_element(By.CSS_SELECTOR, "input#userName").send_keys(data[0])
        # full in name field

        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(data[1])
        # email field

        self.driver.find_element(By.CSS_SELECTOR, "textarea#currentAddress").send_keys(data[2])
        # current address field

        self.driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys(data[3])
        # permanent address field

        element = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        # click submit button

    # verify data presence in output message
    @pytest.mark.text_box
    def test_output(self):
        data_list = DataElements.data_text_box
        elements_list = self.driver.find_elements(By.CLASS_NAME, "mb-1")
        output_list = [element.text for element in elements_list]
        for i in range(0, 4):
            short_text = data_list[i]
            full_text = output_list[i]
            # data[i] in output_list[i]
            self.verify_in_text(short_text, full_text)

    # Suite 3. Test checkbox block on "checkbox" page
    def test_url_checkbox(self, urls):
        self.driver.get(urls["checkbox"])
        self.verify_url("checkbox")

    @pytest.mark.checkbox
    def test_click_dropdown(self):
        # expand main "Home" dropdown and first- and second-level of nested dropdowns
        # once dropdown expended CSS_SELECTOR: "svg...icon-expand-close" -> "svg...icon-expand-open"
        actual = 0
        # actual = count number of clicked dropdown icons
        while True:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, "svg.rct-icon.rct-icon-expand-close")
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                element.click()
                actual += 1

            except NoSuchElementException:
                break

        expect = self.driver.find_elements(By.CSS_SELECTOR, "svg.rct-icon.rct-icon-expand-open")
        self.verify_equal(actual, len(expect))

    @pytest.mark.checkbox
    def test_home_checkbox_message(self):
        # verify success message when "Home" super-checkbox is selected

        self.driver.find_element(By.CSS_SELECTOR, ".rct-checkbox").click()
        # click "Home" checkbox (outcome: all of them, including all nested, should be selected)

        text = self.driver.find_element(By.CSS_SELECTOR, "#result").text
        full_text = text.replace('\n', ' ')
        # remove line break from string extracted from message

        self.verify_in_text("You have selected : home desktop", full_text)

    @pytest.mark.checkbox
    def test_all_checkboxes_selected(self):
        # verify that after clicking on super-checkbox all level checkboxes were selected

        checkboxes_list = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        self.verify_is_selected(checkboxes_list, is_selected=True)

    @pytest.mark.checkbox
    def test_all_checkboxes_unselected(self):
        # verify that after clicking on super-checkbox "home" all level checkboxes were unselected
        self.driver.find_element(By.CSS_SELECTOR, ".rct-checkbox").click()
        # click on first found = "Home"

        checkboxes_list = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        self.verify_is_selected(checkboxes_list, is_selected=False)
        # "is_selected=False" - assertion element not is_selected scenario

    @pytest.mark.checkbox
    def test_random_checkbox_selected(self):
        # verify that a random checkbox can be selected and unselected

        # checkboxes_click_icons = self.driver.find_elements(By.CSS_SELECTOR, "svg.rct-icon.rct-icon-uncheck")
        checkboxes_click_icons = self.driver.find_elements(By.CSS_SELECTOR, ".rct-checkbox")
        # list of elements with clickable checkbox area

        checkboxes_state_list = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        # list of elements with checkboxes selected state attribute

        self.verify_equal(len(checkboxes_click_icons), len(checkboxes_state_list))
        # verify both list contain equal number of elements

        i = random.randrange(0, len(checkboxes_state_list))
        # random index to select an accidental checkbox

        checkboxes_click_icons[i].click()
        self.verify_is_selected(checkboxes_state_list[i], is_selected=True)
        # verify random checkbox was selected

        checkboxes_click_icons[i].click()
        self.verify_is_selected(checkboxes_state_list[i], is_selected=False)
        # verify random checkbox was unselected

    # Suite 4. Test radio-buttons
    @pytest.mark.radio
    def test_url_radio_button(self, urls):
        self.driver.get(urls["radio_button"])
        self.verify_url("radio-button")

    @pytest.mark.radio
    def test_select_radio_buttons(self):
        radio_buttons_click_list = self.driver.find_elements(By.CLASS_NAME, "custom-control-label")
        # list of radio buttons with clickable locators

        radio_buttons_selected_list = self.driver.find_elements(By.CSS_SELECTOR, "input[type='radio'][name='like']")
        # list of radio buttons with input[type='radio'] locators applicable for .is_selected method

        clickable_radios_count = len(radio_buttons_click_list)
        selected_radios_count = len(radio_buttons_selected_list)
        self.verify_equal(clickable_radios_count, selected_radios_count)
        # verify both lists found equal number of radio buttons

        for i in range(0, clickable_radios_count):
            if not radio_buttons_selected_list[i].is_enabled():
                print(f"\n Radio button with index {i} is disable, skipping click.")
                continue

            radio_buttons_click_list[i].click()

            self.verify_is_selected(radio_buttons_selected_list[i], is_selected=True)
            # verify if selected

            if i > 0:
                self.verify_is_selected(radio_buttons_selected_list[i - 1], is_selected=False)
                # verify if previous unselected (=False)

            elif i == clickable_radios_count - 1:
                radio_buttons_click_list[0].click()
                self.verify_is_selected(radio_buttons_selected_list[i], is_selected=False)
                # click first radio button and verify if last one unselected (=False)

    # Suite 5. Test Web Tables
    @pytest.mark.webtables
    def test_url_webtable(self, urls):
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
