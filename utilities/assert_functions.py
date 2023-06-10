import math
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
            message = f"\n Assertion in '{test_func_name}' failed: '{text}' not found in URL."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': '{text}' found in URL."
            print(message)
            log.info(message)

    @staticmethod
    def verify_equal(actual, expect):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            assert actual == expect
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: actual value '{actual}' is not equal to expected '{expect}'."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': '{actual}' value is equal to '{expect}'."
            print(message)
            log.info(message)

    @staticmethod
    def verify_in_text(short_text, full_text):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            assert short_text in full_text
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: text '{short_text}' is not present in full text '{full_text}'."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': '{short_text}' found in full text."
            print(message)
            log.info(message)

    def verify_is_displayed(self, element):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of(element))
            assert element.is_displayed()
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: element not found."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': element displayed."
            print(message)
            log.info(message)

    @staticmethod
    def verify_is_not_displayed(element):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            assert not element.is_displayed()
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: element found."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': element is not displayed."
            print(message)
            log.error(message)

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
                message = f"\n Assertion in '{test_func_name}' failed: element(s) not selected."
                print(message)
                log.error(message)
            else:
                message = f"\n Assertion in '{test_func_name}' failed: element(s) selected."
                print(message)
                log.error(message)
            raise
        else:
            if is_selected:
                message = f"\n Asserted in '{test_func_name}': element(s) selected."
                print(message)
                log.info(message)
            else:
                message = f"\n Asserted in '{test_func_name}': element(s) not selected."
                print(message)
                log.info(message)

    def verify_deleted(self, by, locator):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            assert not self.driver.find_elements(by, locator)
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: element found."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': element deleted."
            print(message)
            log.info(message)

    @staticmethod
    def verify_path_exists(path, timeout):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        # iterate till path to downloaded file exist or timeout is over
        while not os.path.exists(path) and timeout > 0:
            time.sleep(1)
            timeout -= 1

        if os.path.exists(path):
            message = f"\n Assertion in '{test_func_name}': file downloaded successfully!"
            print(message)
            log.info(message)
        else:
            message = f"\n Assertion in '{test_func_name}':File download failed"
            print(message)
            log.error(message)

    @staticmethod
    def verify_enabled(element):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            assert element.is_enabled()
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: element is not enabled."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': element is enabled."
            print(message)
            log.info(message)

    @staticmethod
    def verify_not_enabled(element):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            assert not element.is_enabled()
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: element is enabled."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': element is not enabled."
            print(message)
            log.info(message)

    def verify_image_width(self, image):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        natural_width = self.driver.execute_script("return arguments[0].naturalWidth;", image)
        if natural_width > 0:
            message = f"\n Asserted in '{test_func_name}': image is present with width {natural_width} px."
            print(message)
            log.info(message)
        elif natural_width == 0:
            message = f"\n Assertion in '{test_func_name}' failed: image is broken, width is {natural_width} px."
            print(message)
            log.error(message)
            # raise AssertionError in case of a broken image
            raise AssertionError(message)
        else:
            message = f"\n Something went wrong in '{test_func_name}': image has width '{natural_width}' px."
            print(message)
            log.error(message)
            # raise ValueError for other unexpected cases
            raise ValueError(message)

    # creating custom wait condition to verify a URL change
    class URLChange:
        def __init__(self, driver, original_url):
            # Initializes the class instance with driver and original_url
            self.driver = driver
            self.current_url = original_url

        def __call__(self, driver):
            # Special method to make the instance callable, which verifies the URL change
            return self.driver.current_url != self.current_url

    def verify_url_change(self, by_locator, time_wait):
        # method to verify a URL change after clicking a link
        test_func_name = inspect.stack()[1][3]
        log = self.get_logger()

        original_url = self.driver.current_url
        # saving the current URL as original_url before clicking the link
        try:
            locator_strategy, locator_value = by_locator
            # unpacking 'by_locator' tuple

            # click the link
            link = self.driver.find_element(locator_strategy, locator_value)
            wait = WebDriverWait(self.driver, time_wait)
            wait.until(EC.element_to_be_clickable((locator_strategy, locator_value)))
            link.click()

            url_changes = self.URLChange(self.driver, original_url)
            # creates an instance of URLChange class to verify the URL change

            wait.until(url_changes)
            # waits for the URL to change

            new_url = self.driver.current_url
            # get new URL after clicking the link

            # assert that the new URL is different from the original URL
            assert new_url != original_url
            message = f"\n Asserted in '{test_func_name}': new URL is '{new_url}' and it's different from the original."
            print(message)
            log.info(message)
            return new_url

        except AssertionError:
            message = f"\n Asserted in '{test_func_name}' failed: new URL is '{new_url}' and it's not different from " \
                      f"the original."
            print(message)
            log.error(message)
            raise

    @staticmethod
    def verify_with_tolerance(actual, expected, tolerance):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        try:
            assert math.isclose(actual, expected, rel_tol=tolerance)
        except AssertionError:
            message = f"\n Assertion in '{test_func_name}' failed: actual value '{actual}' with tolerance" \
                      f"'{tolerance}' is not close to expected value '{expected}'."
            print(message)
            log.error(message)
            raise
        else:
            message = f"\n Asserted in '{test_func_name}': '{actual}' value is close to expected value '{expected}' " \
                      f"with tolerance'{tolerance}'."
            print(message)
            log.info(message)

