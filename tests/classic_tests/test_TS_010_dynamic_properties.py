import pytest
from WebInteractionDemoQA.data.test_data import TestData
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.webdriver.common.by import By
import time


# Suite 10. Test Dynamic Properties, Classic Model
class TestDynamicProperties(Assertions, ReusableFunctions):
    @pytest.mark.dynamic_properties
    def test_url_dynamic_properties(self, urls):
        self.driver.get(urls["dynamic_properties"])
        self.verify_url("dynamic-properties")

    @pytest.mark.dynamic_properties
    def test_random_id(self):
        random_id_element = self.driver.find_element(By.CSS_SELECTOR, ".col-12.mt-4.col-md-6 div p")
        self.verify_is_displayed(random_id_element)

    @pytest.mark.dynamic_properties
    def test_enable_with_delay(self):
        # refresh page to disable button
        self.driver.refresh()
        by_locator = (By.CSS_SELECTOR, "button#enableAfter")

        # button should be available in 5 sec
        time_to_wait = 5
        ec_condition = "element_to_be_clickable"

        # call explicit wait
        enabled_element = self.explicitly_wait_for_element(by_locator, time_to_wait, ec_condition)

        # no need to assert since "element_to_be_clickable" condition is already satisfied
        self.verify_enabled(enabled_element)

    @pytest.mark.dynamic_properties
    def test_button_color_change(self):
        self.driver.refresh()
        # to refresh button to its original color

        button = self.driver.find_element(By.ID, "colorChange")

        actual_origin_color = button.value_of_css_property('color')
        self.verify_equal(actual_origin_color, TestData.expected_white)

        time.sleep(5)
        # wait for button to change color

        actual_changed_color = button.value_of_css_property('color')
        self.verify_equal(actual_changed_color, TestData.expected_red)

    @pytest.mark.dynamic_properties
    def test_visible_with_delay(self):
        self.driver.refresh()
        # refresh page to hide button

        self.driver.implicitly_wait(5)
        # wait for 5 seconds for button to be displayed

        button = self.driver.find_element(By.CSS_SELECTOR, "button#visibleAfter")
        self.verify_is_displayed(button)

