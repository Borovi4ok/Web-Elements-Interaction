import inspect
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


# Suite 5. Test Web Tables
class TestWEbTable(Assertions, ReusableFunctions):

    @pytest.mark.webtables
    def test_url_webtable(self, urls):
        self.driver.get(urls["webtables"])
        self.verify_url("webtables")