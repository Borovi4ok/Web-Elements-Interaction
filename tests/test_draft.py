import inspect
import os
import random
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from WebInteractionDemoQA.data.test_data import TestData
import pytest
from WebInteractionDemoQA.page_objects.objects_forms import ObjectsForms
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
import time


@pytest.fixture
def forms_page(setup):
    return ObjectsForms(setup)


# Suite 9. Test Forms
class TestForms(Assertions, ReusableFunctions):

    @pytest.mark.forms
    def test_url_forms(self, urls):
        self.driver.get(urls["forms"])
        self.verify_url("automation-practice-form")

    @pytest.mark.forms
    def test_first_name(self, forms_page):
        first_name = TestData.data_forms["first_name"]
        forms_page.get_first_name().send_keys(first_name)
        value = forms_page.get_first_name().get_attribute("value")
        self.verify_equal(value, first_name)
