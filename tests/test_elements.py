import pytest
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements
from WebInteractionDemoQA.utilities.use_fixtures import Assertions


# text and blocks presence on "elements" page
class TestElementsPage(Assertions):
    @pytest.mark.elements
    def test_url_element(self, urls):
        self.driver.get(urls["elements"])
        self.verify_url("element")
        # to assert, call assert_in_url method in use_fixtures

    @pytest.mark.elements
    def test_header_text(self):
        text_actual = self.driver.find_element(By.CLASS_NAME, "main-header").text
        self.verify_text_equal(text_actual, "Elements")

    @pytest.mark.elements
    def test_main_menu_presence(self):
        element = self.driver.find_element(By.CLASS_NAME, "left-pannel")
        self.verify_is_displayed(element)

    @pytest.mark.elements
    def test_select_message(self):
        text_actual = self.driver.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']").text
        self.verify_text_equal(text_actual, "Please select an item from left to start practice.")

    @pytest.mark.elements
    def test_footer_text(self):
        full_text = self.driver.find_element(By.CSS_SELECTOR, "footer span").text
        self.verify_in_text("ALL RIGHTS RESERVED", full_text)

    # text-box, submit form on "text_box" page
    @pytest.mark.text_box
    def test_url_box(self, urls):
        self.driver.get(urls["text_box"])
        self.verify_url("text-box")

    @pytest.mark.text_box
    def test_submission_form(self):
        # invoke data set from test_data package
        data = DataElements.data_text_box

        # full in name field
        self.driver.find_element(By.CSS_SELECTOR, "input#userName").send_keys(data[0])

        # email field
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(data[1])

        # current address field
        self.driver.find_element(By.CSS_SELECTOR, "textarea#currentAddress").send_keys(data[2])

        # permanent address field
        self.driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys(data[3])

        # click submit button
        element = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

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
