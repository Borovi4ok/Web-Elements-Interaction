from WebInteractionDemoQA.data.test_data import TestData
import pytest
from WebInteractionDemoQA.page_objects.objects_forms import ObjectsForms
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions


@pytest.fixture
def forms_page(setup):
    return ObjectsForms(setup)


# Suite 11. Test Forms, Page Object Model
class TestForms(Assertions, ReusableFunctions):

    @pytest.mark.forms
    def test_url_forms(self, urls):
        self.driver.get(urls["forms"])
        self.verify_url("automation-practice-form")

    @pytest.mark.forms
    def test_first_name(self, forms_page):
        first_name = TestData.data_forms["first_name"]
        forms_page.get_first_name().send_keys(first_name)
        value = forms_page.get_first_name().get_attribute("value")
        self.verify_equal(value, first_name)

    @pytest.mark.forms
    def test_last_name(self, forms_page):
        last_name = TestData.data_forms["last_name"]
        forms_page.get_last_name().send_keys(last_name)
        value = forms_page.get_last_name().get_attribute("value")
        self.verify_equal(value, last_name)

    @pytest.mark.forms
    def test_email(self, forms_page):
        email = TestData.data_forms["email"]
        forms_page.get_email().send_keys(email)
        value = forms_page.get_email().get_attribute("value")
        self.verify_equal(value, email)

    @pytest.mark.forms
    def test_gender_radio(self, forms_page):
        gender = TestData.data_forms["gender"]

        # click radio with respective gender indicated in data_forms
        radio_clickable_list = forms_page.get_gender_radio_click()
        for el in radio_clickable_list:
            # get the label element for the current radio by chaining from it with get_gender_radio_label() method
            el_label = forms_page.get_gender_radio_label(el)
            el_text = el_label.text
            if el_text == gender:
                el.click()

        # verify the respective radio is selected using assertable locators
        radio_assertable_list = forms_page.get_gender_radio_assert()
        for val in radio_assertable_list:
            val_attribute = val.get_attribute("value")
            if val_attribute == gender:
                self.verify_is_selected(val, is_selected=True)

    @pytest.mark.forms
    def test_mobile(self, forms_page):
        mobile = TestData.data_forms["mobile"]
        forms_page.get_mobile().send_keys(mobile)
        value = forms_page.get_mobile().get_attribute("value")
        self.verify_equal(value, mobile)

    @pytest.mark.forms
    def test_date_of_birth(self, forms_page):
        forms_page.get_calendar_dropdown().click()

        # handle month selection
        forms_page.get_calendar_month_dropdown().click()
        month_options = forms_page.get_calendar_month_options()
        month = self.select_match(month_options, TestData.data_forms["month_birth"])
        month.click()

        # handle year selection
        forms_page.get_calendar_year_dropdown().click()
        year_options = forms_page.get_calendar_year_options()
        year = self.select_match(year_options, TestData.data_forms["year_birth"])
        year.click()

        # handle day selection
        day_options = forms_page.get_calendar_day_options()
        day = self.select_match(day_options, TestData.data_forms["day_birth"])
        day.click()

        # verify selected date in field matches with expected
        actual_date = forms_page.get_calendar_dropdown().get_attribute("value")
        expect_date = f"{TestData.data_forms['day_birth']} {TestData.data_forms['month_birth_assert']} {TestData.data_forms['year_birth']}"
        self.verify_equal(actual_date, expect_date)

    @pytest.mark.forms
    def test_subjects_auto_complete(self, forms_page):
        # send part of search value
        subject_short = TestData.data_forms["subject_short"]
        forms_page.get_subjects_auto_complete_field().send_keys(subject_short)

        # wait for suggestions
        by_locator = forms_page.subjects_auto_complete_suggestions
        time_to_wait = 5
        ec_condition = "presence_of_element_located"
        self.explicitly_wait_for_element(by_locator, time_to_wait, ec_condition)

        # get list of suggestions and select the value
        suggestions = forms_page.get_subjects_auto_complete_suggestions()
        subject = self.select_match(suggestions, TestData.data_forms["subject_full"])
        self.scroll_into_view(subject)
        subject.click()

        # verify selected value matches with expected
        subject_actual = forms_page.get_subjects_auto_complete_result()
        self.verify_equal(subject_actual[0].text, TestData.data_forms["subject_full"])

    @pytest.mark.forms
    def test_hobbies_checkboxes(self, forms_page):
        hobby_1 = TestData.data_forms["hobby_1"]
        hobby_2 = TestData.data_forms["hobby_2"]

        # get clickable list of checkboxes and click box(es) indicated in data_forms
        checkboxes_list_clickable = forms_page.get_hobbies_checkboxes_clickable()
        for box in checkboxes_list_clickable:
            self.scroll_into_view(box)
            # get the label element for the current checkbox by chaining from it with get_checkbox_label() method
            box_label = forms_page.get_checkbox_label(box)
            box_text = box_label.text
            if box_text == hobby_1 or box_text == hobby_2:
                box.click()

        # get assertable list of checkboxes and loop it over with "is_selected" assertion
        checkboxes_list_assertable = forms_page.get_hobbies_checkboxes_assertable()
        for val in checkboxes_list_assertable:
            val_attribute = val.get_attribute("value")
            if val_attribute == hobby_1 or val_attribute == hobby_2:
                self.verify_is_selected(val, is_selected=True)

    @pytest.mark.forms
    def test_upload(self, forms_page):
        upload_path = (self.default_download_dir + TestData.file_name)
        forms_page.get_picture_upload().send_keys(upload_path)

    @pytest.mark.forms
    def test_address_box(self, forms_page):
        address = TestData.data_forms["address"]
        text_box = forms_page.get_address_text_area()
        self.scroll_into_view(text_box)
        text_box.send_keys(address)

    @pytest.mark.forms
    def test_state_dropbox(self, forms_page):
        # set window to 700px. wide to interact with web elements covered by advertisement
        self.driver.set_window_size(700, self.driver.execute_script("return window.outerHeight"))

        # state dropdown click
        state_drop = forms_page.get_state_dropdown()
        self.scroll_into_view(state_drop)
        state_drop.click()

        # get list of available state options
        elements_list = forms_page.get_state_options()

        # select state indicated in test data
        state_match = TestData.data_forms["state"]
        state = self.select_match(elements_list, state_match)
        state.click()

        # wait for a locator with selected value to be located
        by_locator = ObjectsForms.state_selected
        self.explicitly_wait_for_element(by_locator, 5, "presence_of_element_located")

        # verify selected state matches expected
        # 'state_elements' returns list
        state_elements = forms_page.get_state_selected()
        state_selected = state_elements[0].text
        self.verify_equal(state_selected, state_match)

    @pytest.mark.forms
    def test_city_dropbox(self, forms_page):
        # city dropdown click
        city_drop = forms_page.get_city_dropdown()
        self.scroll_into_view(city_drop)
        city_drop.click()

        # get list of available city options
        elements_list = forms_page.get_city_options()

        # select city indicated in test data
        city_match = TestData.data_forms["city"]
        city = self.select_match(elements_list, city_match)
        city.click()

        # wait for a locator with selected value to be located
        by_locator = ObjectsForms.city_selected
        self.explicitly_wait_for_element(by_locator, 5, "presence_of_element_located")

        # verify selected city matches expected
        # 'city_elements' returns list
        city_elements = forms_page.get_city_selected()
        city_selected = city_elements[0].text
        self.verify_equal(city_selected, city_match)

    @pytest.mark.forms
    def test_submit_button(self, forms_page):
        forms_page.get_submit_button().click()
        message_actual = forms_page.get_success_message().text
        message_expected = TestData.data_forms["success_message"]
        self.verify_in_text(message_expected, message_actual)

    @pytest.mark.forms
    def test_confirmation_table(self, forms_page):
        # get text from confirmation table (submitted form)
        elements_list = forms_page.get_confirmation()
        values_list = self.extract_text_from_list(elements_list)
        # "values_list" structure - [key, value, key, value ...]

        # modify "data_forms" dictionary to "confirmation_table" order
        expected_confirmation = {
            "Student Name": f"{TestData.data_forms['first_name']} {TestData.data_forms['last_name']}",
            "Student Email": f"{TestData.data_forms['email']}",
            "Gender": f"{TestData.data_forms['gender']}",
            "Mobile": f"{TestData.data_forms['mobile']}",
            "Date of Birth": f"{TestData.data_forms['day_birth']} {TestData.data_forms['month_birth']},{TestData.data_forms['year_birth']}",
            "Subjects": f"{TestData.data_forms['subject_full']}",
            "Hobbies": f"{TestData.data_forms['hobby_1']}, {TestData.data_forms['hobby_2']}",
            "Picture": f"{TestData.file_name}",
            "Address": f"{TestData.data_forms['address']}",
            "State and City": f"{TestData.data_forms['state']} {TestData.data_forms['city']}",
        }

        for i in range(1, len(values_list), 2):
            # every second value starting from [1] in the extracted list
            value = values_list[i]

            # use key from extracted list to call expected value, so key verified as well
            key = values_list[i - 1]

            self.verify_equal(value, expected_confirmation[key])
