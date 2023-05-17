import inspect
import os
import random
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from WebInteractionDemoQA.data.test_data import TestData
from selenium.webdriver.chrome.options import Options
import pytest
from WebInteractionDemoQA.data.excel_data import get_excel_data
from WebInteractionDemoQA.page_objects.objects_TS_014_frames import Frames
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
import time
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def frames_page(setup):
    return Frames(setup)


# Suite 14. Test Frames, Page Object Model
class TestFrames(Assertions, ReusableFunctions):
    @pytest.mark.frames
    def test_url_frames(self, urls, get_excel_data):
        self.driver.get(urls["frames"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("014_url_frames", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.frames
    def test_iframe_1(self, frames_page, get_excel_data):
        iframe = frames_page.get_iframe_1()
        self.driver.switch_to.frame(iframe)
        text_element = frames_page.get_text_iframe_1()
        text = text_element.text
        full_text = get_excel_data("014_iframe_1", "text_verify")
        self.verify_in_text(text, full_text)
        self.driver.switch_to.default_content()

    @pytest.mark.frames
    def test_iframe_2(self, frames_page, get_excel_data):
        # test second iframe by switching to it getting list of all iframes on the page
        iframes = frames_page.get_iframes()  # list of found iframes on the page
        found_iframes = len(iframes)

        # call reusable function "log_print" to log the message with respective log level
        message = f"found {found_iframes} iframes on the page"
        info = "info"
        self.log_print(info, message)

        # switch to the second iframe in the list
        self.driver.switch_to.frame(iframes[1])

        text_element = frames_page.get_text_iframe_2()
        text = text_element.text
        full_text = get_excel_data("014_iframe_2", "text_verify")
        self.verify_in_text(text, full_text)
        self.driver.switch_to.default_content()
