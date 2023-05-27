import pytest

from WebInteractionDemoQA.page_objects.objects_TS_019_date_picker import DatePicker
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
from WebInteractionDemoQA.page_objects.objects_TS_014_frames import Frames
from WebInteractionDemoQA.page_objects.objects_TS_015_nested_frames import NestedFrames
from WebInteractionDemoQA.page_objects.objects_TS_016_modal_dialogs import ModalDialogs
from WebInteractionDemoQA.page_objects.objects_TS_018_auto_complete import AutoComplete
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def date_picker_page(setup):
    return DatePicker(setup)


# Suite 19. Test Date Picker, Page Object Model
class TestDatePicker(Assertions, ReusableFunctions):
    @pytest.mark.date_picker
    def test_url_date_picker(self, urls, get_excel_data):
        self.driver.get(urls["date_picker"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("019_url_date_picker", "text_verify")
        self.verify_url(expected_url)

    """
    @pytest.mark.date_picker
    def test_date_picker(self, date_picker_page, get_excel_data):
        date_box = date_picker_page.get_date_box()
        date_box.click()

        # testing date from Excel sheet
        # format Month DD YYYY
        testing_date = get_excel_data("019_date_picker", "text_verify")

        # select year
        years = date_picker_page.get_years()
        tested_year = testing_date.split(" ")[2]
        year_match = self.select_match(years, tested_year)  # call reusable function to loop through years list
        year_match.click()

        # select month
        months = date_picker_page.get_months()
        tested_month = testing_date.split(" ")[0]
        month_match = self.select_match(months, tested_month)  # call reusable function to loop through months list
        month_match.click()

        # select day
        day = date_picker_page.get_days()
        tested_day = testing_date.split(" ")[1]
        day_match = self.select_match(day, tested_day)  # call reusable function to loop through days list
        day_match.click()

        # verify date selected
        selected_date = date_picker_page.get_date_box().get_attribute('value')
        date = datetime.strptime(testing_date, "%B %d %Y")
        # convert the date string to a datetime object

        formatted_date = date.strftime("%m/%d/%Y")
        # format the datetime object to the format of 'value' attribute of the 'input' element

        self.verify_equal(selected_date, formatted_date)
    """

    @pytest.mark.date_picker
    def test_date_and_time_picker(self, date_picker_page, get_excel_data):
        date_picker_page.get_date_and_time_box().click()

        # select year
        date_picker_page.get_year_tab().click()
        year_options = date_picker_page.get_year_options()
        # list of visible years

        length_year_options = len(year_options)
        message = ""

        # testing date from Excel sheet
        # format Month DD YYYY
        testing_date = get_excel_data("019_date_and_time_picker", "text_verify")
        testing_year = testing_date.split(" ")[2]

        # check if testing year is visible right away
        year_visible = False
        for i in range(1, length_year_options - 1):
            # very first and very last element are up/down arrows
            if testing_year in year_options[i].text:
                message = f"Selected year is '{year_options[i].text}'"
                year_options[i].click()
                year_visible = True
                break

        # if testing year is not visible click down to dynamically create desired year
        if not year_visible:
            i = length_year_options - 2
            last_visible_year = year_options[i].text
            # the very first and very last contain up/down scroll arrows

            difference = int(last_visible_year) - int(testing_year)
            ind = 0
            while ind != difference:
                down_arrow = date_picker_page.get_years_scroll_down()
                self.scroll_into_view(down_arrow)
                down_arrow.click()
                ind += 1

            new_last_visible_year = date_picker_page.get_last_visible_year()
            message = f"Selected year is '{new_last_visible_year.text}'"
            new_last_visible_year.click()

        self.log_print("info", message)
