import pytest
from selenium.webdriver.common.action_chains import ActionChains
from WebInteractionDemoQA.page_objects.objects_TS_019_date_picker import DatePicker
from WebInteractionDemoQA.page_objects.objects_TS_020_slider import Slider
from WebInteractionDemoQA.page_objects.objects_TS_023_tooltips import Tooltips
from WebInteractionDemoQA.page_objects.objects_TS_025_select_menu import SelectMenu
from WebInteractionDemoQA.page_objects.objects_TS_026_sortable import Sortable
from WebInteractionDemoQA.page_objects.objects_TS_027_selectable import Selectable
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
def selectable_page(setup):
    return Selectable(setup)


# Suite 27. Test Selectable, Page Object Model
class TestSelectable(Assertions, ReusableFunctions):
    @pytest.mark.selectable
    def test_url_selectable(self, urls, get_excel_data):
        self.driver.get(urls["selectable"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("027_url_selectable", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.selectable
    def test_selectable_list(self, selectable_page, get_excel_data):
        list_items = selectable_page.get_list_items()

       