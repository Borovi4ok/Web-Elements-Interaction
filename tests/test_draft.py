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

    @pytest.mark.forms
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
        gender = TestData.data_forms["gender"]

        # click radio with respective gender indicated in data_forms
        radio_clickable_list = forms.get_gender_radio_click()
        for el in radio_clickable_list:
            # get the label element for the current radio by chaining from it with get_gender_radio_label() method
            el_label = forms.get_gender_radio_label(el)
            el_text = el_label.text
            if el_text == gender:
                el.click()

        # verify the respective radio is selected using assertable locators
        radio_assertable_list = forms.get_gender_radio_assert()
        for val in radio_assertable_list:
            val_attribute = val.get_attribute("value")
            if val_attribute == gender:
                self.verify_is_selected(val, is_selected=True)

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
        text_box.send_keys(address)

    @pytest.mark.forms
    def test_state_dropbox(self):
        forms = ObjectsForms(self.driver)

        # set window to 700px. wide to interact with web elements covered by advertisement
        self.driver.set_window_size(700, self.driver.execute_script("return window.outerHeight"))

        # state dropdown click
        state_drop = forms.get_state_dropdown()
        self.scroll_into_view(state_drop)
        state_drop.click()

        # get list of available state options
        elements_list = forms.get_state_options()

        # select state indicated in test data
        state_match = TestData.data_forms["state"]
        state = self.select_match(elements_list, state_match)
        state.click()

        # wait for a locator with selected value to be located
        by_locator = ObjectsForms.state_selected
        self.explicitly_wait_for_element(by_locator, 5, "presence_of_element_located")

        # verify selected state matches expected
        # 'state_elements' returns list
        state_elements = forms.get_state_selected()
        state_selected = state_elements[0].text
        self.verify_equal(state_selected, state_match)

    @pytest.mark.forms
    def test_city_dropbox(self):
        forms = ObjectsForms(self.driver)

        # city dropdown click
        city_drop = forms.get_city_dropdown()
        self.scroll_into_view(city_drop)
        city_drop.click()

        # get list of available city options
        elements_list = forms.get_city_options()

        # select city indicated in test data
        city_match = TestData.data_forms["city"]
        city = self.select_match(elements_list, city_match)
        city.click()

        # wait for a locator with selected value to be located
        by_locator = ObjectsForms.city_selected
        self.explicitly_wait_for_element(by_locator, 5, "presence_of_element_located")

        # verify selected city matches expected
        # 'city_elements' returns list
        city_elements = forms.get_city_selected()
        city_selected = city_elements[0].text
        self.verify_equal(city_selected, city_match)

    @pytest.mark.forms
    def test_submit_button(self):
        forms = ObjectsForms(self.driver)
        forms.get_submit_button().click()
        message_actual = forms.get_success_message().text
        message_expected = TestData.data_forms["success_message"]
        self.verify_in_text(message_expected, message_actual)

    """@pytest.mark.forms
    def test_confirmation_table(self):
        forms = ObjectsForms(self.driver)

        # get text from confirmation table (submitted form)
        elements_list = forms.get_confirmation()
        values_list = self.extract_text_from_list(elements_list)
        # "values_list" structure - [key, value, ...]

        # modify "data_forms" dictionary to "confirmation_table" order
        expected_confirmation = {
            "Student Name"
        }
    
    
    
    # example of GPT, but should do myself
        expected_values = {
    "Student Name": f"{data_forms['first_name']} {data_forms['last_name']}",
    "Student Email": data_forms["email"],
    "Mobile": data_forms["mobile"],
    "Date of Birth": f"{data_forms['day_birth']} {data_forms['month_birth']},{data_forms['year_birth']}",
    "Subjects": data_forms["subject_full"],
    "Address": data_forms["address"],
    "State and City": f"{data_forms['state']} {data_forms['city']}"


    for i in range(0, len(confirm_list), 2):
        key = confirm_list[i]
        value = confirm_list[i+1]
        assert value == expected_values[key]
        

    def test_radio(self):
        lista = self.driver.find_elements(By.XPATH, "//div[@class='custom-control custom-radio custom-control-inline']/label")
        for element in lista:
            print(element.text)"""




