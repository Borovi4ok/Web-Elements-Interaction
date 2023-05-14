import inspect
import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from WebInteractionDemoQA.utilities.assert_functions import Assertions


@pytest.mark.usefixtures("setup")
class ReusableFunctions:

    def get_column_data(self, column_data, as_int=True):
        # as_int parameter to return digits as: if True = int, if False = str

        items_list = []
        # items_list - extracted text, removed empty strings, digits converted in int or str
        for data in column_data:
            text = data.text
            if text.strip() and not text.isdigit():

                items_list.append(text)
            elif text.isdigit():
                if as_int:
                    items_list.append(int(text))
                else:
                    items_list.append(text)
        return items_list
        # returns list of items (str of int) in a column with a corresponding 'ind'

    @staticmethod
    def clear_and_fill_in(range_min, range_max, list_to_edit, data_list):
        # refill each line in a form
        for i in range(range_min, range_max):
            list_to_edit[i].clear()
            list_to_edit[i].send_keys(data_list[i])

    @staticmethod
    def extract_text_from_list(elements_list):
        text_list = [element.text for element in elements_list]
        return text_list

    @staticmethod
    def get_random_number(maximum):
        random_number = random.randrange(0, maximum)
        return random_number

    @staticmethod
    def select_match(elements, match):
        for element in elements:
            if element.text == match:
                return element

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def explicitly_wait(self, by_locator, time_to_wait, ec_condition):
        # if wait for an element, argument to pass (by_locator, time_to_wait, ec_condition)
        # if wait does not involve element, (False, time_to_wait, ec_condition)

        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()
        wait = WebDriverWait(self.driver, time_to_wait)

        # "wait for element" block
        if by_locator:
            # unpack 'by_locator' Tuple
            locator_strategy, locator_value = by_locator

            try:
                element = self.driver.find_element(locator_strategy, locator_value)
                wait.until(getattr(EC, ec_condition)((locator_strategy, locator_value)))
                """getattr - dynamically retrieves an attribute from EC class based on the value of the ec_condition 
                parameter"""
                message = f"\n For '{test_func_name}': EC condition '{ec_condition}' satisfied within {time_to_wait}sec."
                print(message)
                log.info(message)
                return element

            except NoSuchElementException:
                message = f"\n For '{test_func_name}': EC condition '{ec_condition}' is not satisfied within {time_to_wait} sec."
                print(message)
                log.info(message)
                raise
        # "wait for a condition without element" block
        else:
            try:
                wait.until(getattr(EC, ec_condition)())
                message = f"\n For '{test_func_name}': EC condition '{ec_condition}' satisfied within {time_to_wait} sec."
                print(message)
                log.info(message)

            except TimeoutException:
                message = f"\n For '{test_func_name}': EC condition '{ec_condition}' is not satisfied within {time_to_wait} sec."
                print(message)
                log.info(message)
                raise
