import pytest
from selenium.webdriver.common.action_chains import ActionChains
from WebInteractionDemoQA.page_objects.objects_TS_019_date_picker import DatePicker
from WebInteractionDemoQA.page_objects.objects_TS_020_slider import Slider
from WebInteractionDemoQA.page_objects.objects_TS_023_tooltips import Tooltips
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from datetime import datetime
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
from WebInteractionDemoQA.page_objects.objects_TS_017_accordion import Accordion
import time
from WebInteractionDemoQA.data.excel_data import get_excel_data
from WebInteractionDemoQA.page_objects.objects_TS_024_menu import Menu
from WebInteractionDemoQA.page_objects.objects_TS_015_nested_frames import NestedFrames
from WebInteractionDemoQA.page_objects.objects_TS_016_modal_dialogs import ModalDialogs
from WebInteractionDemoQA.page_objects.objects_TS_018_auto_complete import AutoComplete
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def menu_page(setup):
    return Menu(setup)


# Suite 24. Test Menu, Page Object Model
class TestMenu(Assertions, ReusableFunctions):
    @pytest.mark.menu
    def test_url_menu(self, urls, get_excel_data):
        self.driver.get(urls["menu"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("024_url_menu", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.menu
    def test_main_item_1(self, menu_page):
        main_item_1 = menu_page.get_main_item_1()
        self.verify_enabled(main_item_1)

    @pytest.mark.menu
    def test_dropdown_main_item_2(self, menu_page, get_excel_data):
        main_item_2 = menu_page.get_main_item_2()

        # move to the menu-2 dropdown and wait it expands
        actions = ActionChains(self.driver)
        actions.move_to_element(main_item_2).perform()
        by_locator = menu_page.sub_items
        self.explicitly_wait(by_locator, 5, "visibility_of_element_located")

        # get list of all sub-items and sub-sub items in dropdown
        sub_items = menu_page.get_sub_items()

        # expand sub-sub items
        expandable_menu_item = get_excel_data("024_dropdown_main_item_2", "text_verify")
        for item in sub_items:
            if expandable_menu_item in item.text:
                actions.move_to_element(item).perform()
                break

        # wait for sub-sub items to expand
        by_locator = menu_page.sub_sub_items
        self.explicitly_wait(by_locator, 5, "visibility_of_element_located")

        # verify all sub and sub-sub items are visible and enabled for click
        for item in sub_items:
            message = f"Verifying for menu-item '{item.text}'"
            self.log_print("info", message)
            self.verify_is_displayed(item)
            self.verify_enabled(item)

    @pytest.mark.menu
    def test_main_item_3(self, menu_page):
        main_item_3 = menu_page.get_main_item_3()
        self.verify_enabled(main_item_3)