import pytest
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.data.test_data import TestData
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions


# Suite 2. Test text-box submit form on "text_box" page
class TestTextBox(Assertions, ReusableFunctions):
    @pytest.mark.text_box
    def test_url_box(self, urls):
        self.driver.get(urls["text_box"])
        self.verify_url("text-box")

    @pytest.mark.text_box
    def test_submission_form(self):
        # invoke data-list set from test_data package
        data = TestData.data_text_box

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
    def test_box_output(self):
        data_list = TestData.data_text_box
        elements_list = self.driver.find_elements(By.CLASS_NAME, "mb-1")
        output_list = [element.text for element in elements_list]
        for i in range(0, 4):
            short_text = data_list[i]
            full_text = output_list[i]
            # data[i] in output_list[i]
            self.verify_in_text(short_text, full_text)
