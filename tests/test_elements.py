import pytest
import random
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements
from WebInteractionDemoQA.utilities.use_fixtures import Assertions
from selenium.common.exceptions import NoSuchElementException


class TestElementsPage(Assertions):
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
