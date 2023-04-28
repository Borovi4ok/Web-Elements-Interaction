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


# Suite 9. Test Forms
class TestForms(Assertions, ReusableFunctions):

    @pytest.mark.forms
    def test_url_forms(self, urls):
        self.driver.get(urls["forms"])
        self.verify_url("automation-practice-form")

    """@pytest.mark.forms
    def test_first_name(self):
        forms = ObjectsForms(self.driver)
        first_name = TestData.data_forms["first_name"]
        forms.get_first_name().send_keys(first_name)
        value = forms.get_first_name().get_attribute("value")
        self.verify_equal(value, first_name)

    @pytest.mark.forms
    def test_last_name(self):
        forms = ObjectsForms(self.driver)
        last_name = TestData.data_forms["last_name"]
        forms.get_last_name().send_keys(last_name)
        value = forms.get_last_name().get_attribute("value")
        self.verify_equal(value, last_name)

    @pytest.mark.forms
    def test_email(self):
        forms = ObjectsForms(self.driver)
        email = TestData.data_forms["email"]
        forms.get_email().send_keys(email)
        value = forms.get_email().get_attribute("value")
        self.verify_equal(value, email)

    @pytest.mark.forms
    def test_gender_radio(self):
        forms = ObjectsForms(self.driver)
        ran = TestData.random
        # random number to click any radio

        radio_clickable_list = forms.get_gender_radio_click()
        radio_clickable_list[ran].click()
        # select random radio

        radio_assertable_list = forms.get_gender_radio_assert()
        self.verify_is_selected(radio_assertable_list[ran], is_selected=True)
        # verify selected radio with index [ran] is selected

    @pytest.mark.forms
    def test_mobile(self):
        forms = ObjectsForms(self.driver)
        mobile = TestData.data_forms["mobile"]
        forms.get_mobile().send_keys(mobile)
        value = forms.get_mobile().get_attribute("value")
        self.verify_equal(value, mobile)

    @pytest.mark.forms
    def test_date_of_birth(self):
        forms = ObjectsForms(self.driver)
        forms.get_calendar_dropdown().click()

        # handle month selection
        forms.get_calendar_month_dropdown().click()
        month_options = forms.get_calendar_month_options()
        month = self.select_match(month_options, TestData.data_forms["month_birth"])
        month.click()

        # handle year selection
        forms.get_calendar_year_dropdown().click()
        year_options = forms.get_calendar_year_options()
        year = self.select_match(year_options, TestData.data_forms["year_birth"])
        year.click()

        # handle day selection
        day_options = forms.get_calendar_day_options()
        day = self.select_match(day_options, TestData.data_forms["day_birth"])
        day.click()

        # verify selected date in field matches with expected
        actual_date = forms.get_calendar_dropdown().get_attribute("value")
        expect_date = f"{TestData.data_forms['day_birth']} {TestData.data_forms['month_birth_assert']} {TestData.data_forms['year_birth']}"
        self.verify_equal(actual_date, expect_date)

    @pytest.mark.forms
    def test_subjects_auto_complete(self):
        forms = ObjectsForms(self.driver)

        # send part of search value
        subject_short = TestData.data_forms["subject_short"]
        forms.get_subjects_auto_complete_field().send_keys(subject_short)

        # wait for suggestions
        by_locator = forms.subjects_auto_complete_suggestions
        time_to_wait = 5
        ec_condition = "presence_of_element_located"
        self.explicitly_wait_for_element(by_locator, time_to_wait, ec_condition)

        # get list of suggestions and select the value
        suggestions = forms.get_subjects_auto_complete_suggestions()
        subject = self.select_match(suggestions, TestData.data_forms["subject_full"])
        self.scroll_into_view(subject)
        subject.click()

        # verify selected value matches with expected
        subject_actual = forms.get_subjects_auto_complete_result()
        self.verify_equal(subject_actual[0].text, TestData.data_forms["subject_full"])

    @pytest.mark.forms
    def test_hobbies_check_boxes(self):
        forms = ObjectsForms(self.driver)

        # get clickable list of checkboxes and loop it over with click
        check_boxes_list_clickable = forms.get_hobbies_check_boxes_clickable()
        for box in check_boxes_list_clickable:
            self.scroll_into_view(box)
            box.click()
            
        # get assertable list of checkboxes and loop it over with "is_selected" assertion
        check_boxes_list_assertable = forms.get_hobbies_check_boxes_assertable()
        for box in check_boxes_list_assertable:
            self.verify_is_selected(box, is_selected=True)

    @pytest.mark.forms
    def test_upload(self):
        forms = ObjectsForms(self.driver)
        upload_path = (self.default_download_dir + TestData.file_name)
        forms.get_picture_upload().send_keys(upload_path)

    @pytest.mark.forms
    def test_address_box(self):
        forms = ObjectsForms(self.driver)
        address = TestData.data_forms["address"]
        text_box = forms.get_address_text_area()
        self.scroll_into_view(text_box)
        text_box.send_keys(address)"""

    @pytest.mark.forms
    def test_state_dropbox(self):
        # set window to 700px. wide to interact with web elements covered by advertisement
        self.driver.set_window_size(700, self.driver.execute_script("return window.outerHeight"))

        time.sleep(10)
        print("finishing")



