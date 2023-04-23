import inspect
import os
import random
import pytest
from selenium.common import NoSuchElementException

from WebInteractionDemoQA.data.test_data import TestData
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


# Suite 8. Test Dynamic Properties
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



