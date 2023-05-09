import pytest
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions


# Suite 1. Test blocks and text presence on "Elements" page, Classic Model
class TestElementsPage(Assertions, ReusableFunctions):
    @pytest.mark.elements
    def test_url_element(self, urls):
        self.driver.get(urls["elements"])
        self.verify_url("element")
        # to assert, verify_url method in use_fixtures

    @pytest.mark.elements
    def test_header_text(self):
        self.driver.implicitly_wait(10)
        actual = self.driver.find_element(By.CLASS_NAME, "main-header").text
        # actual = self.wait_for_element(By.CLASS_NAME, "main-header").text
        self.driver.implicitly_wait(10)
        self.verify_equal(actual, "Elements")

    @pytest.mark.elements
    def test_main_menu_presence(self):
        element = self.driver.find_element(By.CLASS_NAME, "left-pannel")
        # element = self.wait_for_element(By.CLASS_NAME, "left-pannel")
        self.verify_is_displayed(element)

    @pytest.mark.elements
    def test_select_message(self):
        actual = self.driver.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']").text
        # actual = self.wait_for_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']")
        self.verify_equal(actual, "Please select an item from left to start practice.")

    @pytest.mark.elements
    def test_footer_text(self):
        full_text = self.driver.find_element(By.CSS_SELECTOR, "footer span").text
        # full_text = self.wait_for_element(By.CSS_SELECTOR, "footer span").text
        self.verify_in_text("ALL RIGHTS RESERVED", full_text)

