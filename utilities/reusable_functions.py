import inspect
import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from WebInteractionDemoQA.utilities.assert_functions import Assertions


@pytest.mark.usefixtures("setup")
class ReusableFunctions:

    def get_column_data(self, ind, as_int=True):
        column_data = self.driver.find_elements(By.XPATH, f"//div[@class='rt-tr-group']//div[@class='rt-td'][{ind}]")
        # data from any given column in table depending on 'ind'
        # 'ind' = index for a column selector, (in DOM row (class='rt-td') number in order)
        # as_int parameter to return digits as: if True = int, if False = str

        items_list = []
        # items_list - extracted text, removed empty strings, digits converted in int or str
        for item in column_data:
            text = item.text
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

    def explicitly_wait_for_element(self, by_locator, time_to_wait, ec_condition):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        # unpack 'by_locator' Tuple
        locator_strategy, locator_value = by_locator
        try:
            element = self.driver.find_element(locator_strategy, locator_value)
            wait = WebDriverWait(self.driver, time_to_wait)

            # getattr - dynamically retrieve ExpectedCondition method based on the value of the ec_condition parameter
            wait.until(getattr(EC, ec_condition)((locator_strategy, locator_value)))
            print(f"\n For '{test_func_name}': EC condition '{ec_condition}' satisfied within {time_to_wait} sec.")
            log.info(f"\n For '{test_func_name}': EC condition '{ec_condition}' satisfied within {time_to_wait} sec.")
            return element
        except NoSuchElementException:
            print(
                f"\n For '{test_func_name}': EC condition '{ec_condition}' is not satisfied within {time_to_wait} sec.")
            log.info(
                f"\n For '{test_func_name}': EC condition '{ec_condition}' is not satisfied within {time_to_wait} sec.")
            raise

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