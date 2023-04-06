import pytest
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements
from WebInteractionDemoQA.utilities.use_fixtures import BaseClass


# from WebInteractionDemoQA.utilities import use_fixtures


# text and blocks presence on "elements" page
# key to run is "elements"
class TestElementsPage(BaseClass):
    def test_url_elements(self, urls):
        self.driver.get(urls["elements"])

        # to assert, call assert_in_url method in use_fixtures
        self.assert_in_url("element")


    def test_main_header_text_elements(self):
        text = self.driver.find_element(By.CLASS_NAME, "main-header").text
        assert text == "Elements"


    def test_main_menu_presence_elements(self):
        box = self.driver.find_element(By.CLASS_NAME, "left-pannel")
        assert box.is_displayed()


    def test_select_message_elements(self):
        text = self.driver.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']").text
        assert text == "Please select an item from left to start practice."


    def test_footer_text_elements(self):
        text = self.driver.find_element(By.CSS_SELECTOR, "footer span").text
        assert "ALL RIGHTS RESERVED" in text


    # text-box, submit form on "text_box" page
    # key in names is "text_box"
    def test_url_text_box(self, urls):
        self.driver.get(urls["text_box"])
        assert "text-box" in self.driver.current_url


    def test_text_box(self):
        # invoke data set from test_data package
        data = DataElements.data_text_box

        # fill out text-box
        # full name field
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


    # verify passed data is present in output message
    def test_output_text_box(self):
        data = DataElements.data_text_box
        elements_list = self.driver.find_elements(By.CLASS_NAME, "mb-1")
        output_list = [element.text for element in elements_list]
        for i in range(0, 4):
            assert data[i] in output_list[i]