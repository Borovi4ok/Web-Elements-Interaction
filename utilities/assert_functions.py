import os
import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
import inspect
import logging

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Assertions:
    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        if not logger.handlers:
            file_handler = logging.FileHandler("logfile.log")
            formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)
        return logger

    def verify_url(self, text):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        try:
            assert text in self.driver.current_url
        except AssertionError:
            print(f"\n Assertion in '{test_func_name}' failed: '{text}' not found in URL.")
            log.error(f"\n Assertion in '{test_func_name}' failed: '{text}' not found in URL.")
            raise
        else:
            print(f"\n Asserted in '{test_func_name}': '{text}' found in URL.")
            log.info(f"\n Asserted in '{test_func_name}': '{text}' found in URL.")

    @staticmethod
    def verify_equal(actual, expect):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        try:
            assert actual == expect
        except AssertionError:
            print(
                f"\n Assertion in '{test_func_name}' failed: actual value '{actual}' is not equal to expected '{expect}'.")
            log.error(
                f"\n Assertion in '{test_func_name}' failed: actual value '{actual}' is not equal to expected '{expect}'.")
            raise
        else:
            print(f"\n Asserted in '{test_func_name}': '{actual}' value is equal to '{expect}.")
            log.info(f"\n Asserted in '{test_func_name}': '{actual}' value is equal to '{expect}'.")

    @staticmethod
    def verify_in_text(short_text, full_text):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        try:
            assert short_text in full_text
        except AssertionError:
            print(
                f"\n Assertion in '{test_func_name}' failed: text '{short_text}' is not present in full text '{full_text}'.")
            log.error(
                f"\n Assertion in '{test_func_name}' failed: text '{short_text}' is not present in full text '{full_text}'.")
            raise
        else:
            print(f"\n Asserted in '{test_func_name}': '{short_text}' found in full text.")
            log.info(f"\n Asserted in '{test_func_name}': '{short_text}' found in full text.")

    def verify_is_displayed(self, element):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of(element))
            assert element.is_displayed()
        except AssertionError:
            print(f"\n Assertion in '{test_func_name}' failed: element not found.")
            log.error(f"\n Assertion in '{test_func_name}' failed: element not found.")
            raise
        else:
            print(f"\n Asserted in '{test_func_name}': element displayed.")
            log.info(f"\n Asserted in '{test_func_name}': element displayed.")

    @staticmethod
    def verify_is_selected(element, is_selected=True):
        # if "is_selected=True": verify is_selected() scenario
        # else "is_selected=False" verify not is_selected() scenario
        # i = number of iterations (count of asserted elements)

        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        try:
            if isinstance(element, list):
                i = 0
                for elm in element:
                    if is_selected:
                        assert elm.is_selected()
                    else:
                        assert not elm.is_selected()
                    i += 1
                # print(f"Number of found elements = {i}")
                log.info(f"'{test_func_name}': Number of found elements = {i}")
            else:
                if is_selected:
                    assert element.is_selected()
                else:
                    assert not element.is_selected()
        # if element is list - loop through and assert each, else - just assert

        except AssertionError:
            if is_selected:
                print(f"\n Assertion in '{test_func_name}' failed: element(s) not selected.")
                log.error(f"\n Assertion in '{test_func_name}' failed: element(s) not selected.")
            else:
                print(f"\n Assertion in '{test_func_name}' failed: element(s) selected.")
                log.error(f"\n Assertion in '{test_func_name}' failed: element(s) selected.")
            raise
        else:
            if is_selected:
                print(f"\n Asserted in '{test_func_name}': element(s) selected.")
                log.info(f"\n Asserted in '{test_func_name}': element(s) selected.")
            else:
                print(f"\n Asserted in '{test_func_name}': element(s) not selected.")
                log.info(f"\n Asserted in '{test_func_name}': element(s) not selected.")

    def verify_deleted(self, by, locator):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        try:
            assert not self.driver.find_elements(by, locator)
        except AssertionError:
            print(f"\n Assertion in '{test_func_name}' failed: element found.")
            log.error(f"\n Assertion in '{test_func_name}' failed: element found.")
            raise
        else:
            print(f"\n Asserted in '{test_func_name}': element deleted.")
            log.info(f"\n Asserted in '{test_func_name}': element deleted.")

    @staticmethod
    def verify_path_exists(path, timeout):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        # iterate till path to downloaded file exist or timeout is over
        while not os.path.exists(path) and timeout > 0:
            time.sleep(1)
            timeout -= 1

        if os.path.exists(path):
            print(f"\n Assertion in '{test_func_name}': file downloaded successfully!")
            log.info(f"\n Assertion in '{test_func_name}': file downloaded successfully!")
        else:
            print(f"\n Assertion in '{test_func_name}':File download failed")
            log.error(f"\n Assertion in '{test_func_name}':File download failed")

    @staticmethod
    def verify_enabled(element):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        try:
            assert element.is_enabled()
        except AssertionError:
            print(f"\n Assertion in '{test_func_name}' failed: element is not enabled.")
            log.error(f"\n Assertion in '{test_func_name}' failed: element is not enabled.")
            raise
        else:
            print(f"\n Asserted in '{test_func_name}': element is enabled.")
            log.info(f"\n Asserted in '{test_func_name}': element is enabled.")
