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


# Suite 9. Test Forms
class TestDynamicProperties(Assertions, ReusableFunctions):
    @pytest.mark.dynamic_properties
    def test_url_dynamic_properties(self, urls):
        self.driver.get(urls["dynamic_properties"])
        self.verify_url("dynamic-properties")


