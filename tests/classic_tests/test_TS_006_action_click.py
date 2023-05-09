import pytest
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.webdriver.common.by import By


# Suite 6. Test Action Click, Classic Model
class TestActionClick(Assertions, ReusableFunctions):
    @pytest.mark.action_click
    def test_url_action(self, urls):
        self.driver.get(urls["buttons"])
        self.verify_url("buttons")

    @pytest.mark.action_click
    def test_action_double_click(self, action_chains):
        action_chains.double_click(self.driver.find_element(By.ID, "doubleClickBtn")).perform()
        success_message = self.driver.find_element(By.ID, "doubleClickMessage")
        self.verify_is_displayed(success_message)

    @pytest.mark.action_click
    def test_action_right_click(self, action_chains):
        action_chains.context_click(self.driver.find_element(By.ID, "rightClickBtn")).perform()
        success_message = self.driver.find_element(By.ID, "rightClickMessage")
        self.verify_is_displayed(success_message)

    @pytest.mark.action_click
    def test_action_dynamic_click(self):
        self.driver.find_element(By.XPATH, "//button[@type='button' and text()='Click Me']").click()
        success_message = self.driver.find_element(By.ID, "dynamicClickMessage")
        self.verify_is_displayed(success_message)