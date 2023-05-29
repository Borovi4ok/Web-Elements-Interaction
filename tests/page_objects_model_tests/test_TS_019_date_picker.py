import pytest
from WebInteractionDemoQA.page_objects.objects_TS_019_date_picker import DatePicker
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from datetime import datetime
from selenium.common import NoSuchElementException
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

    @pytest.mark.date_picker
    def test_date_picker(self, date_picker_page, get_excel_data):
        date_box = date_picker_page.get_date_box()
        date_box.click()

        # testing date from Excel sheet
        # format Month DD YYYY
        testing_date = get_excel_data("019_date_picker", "text_verify")

        # select year
        years = date_picker_page.get_years()
        testing_year = testing_date.split(" ")[2]
        year_match = self.select_match(years, testing_year)  # call reusable function to loop through years list
        year_match.click()

        # select month
        months = date_picker_page.get_months()
        testing_month = testing_date.split(" ")[0]
        month_match = self.select_match(months, testing_month)  # call reusable function to loop through months list
        month_match.click()

        # select day
        days = date_picker_page.get_days()
        testing_day = testing_date.split(" ")[1]
        day_match = self.select_match(days, testing_day)  # call reusable function to loop through days list
        day_match.click()

        # verify date selected
        selected_date = date_picker_page.get_date_box().get_attribute('value')
        date = datetime.strptime(testing_date, "%B %d %Y")
        # convert the date string to a datetime object

        formatted_date = date.strftime("%m/%d/%Y")
        # format the datetime object to the format of 'value' attribute of the 'input' element

        self.verify_equal(selected_date, formatted_date)

    # test date and time picker separately
    @pytest.mark.date_picker
    def test_dt_year(self, date_picker_page, get_excel_data):
        date_picker_page.get_date_and_time_box().click()

        # select year
        date_picker_page.get_dt_year_tab().click()
        year_options = date_picker_page.get_dt_year_options()  # list of visible years

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
            last_visible_year = year_options[i].text  # the very first and very last contain up/down scroll arrows

            difference = int(last_visible_year) - int(testing_year)
            ind = 0
            while ind != difference:
                down_arrow = date_picker_page.get_dt_years_scroll_down()
                self.scroll_into_view(down_arrow)
                down_arrow.click()
                ind += 1

            new_last_visible_year = date_picker_page.get_dt_year_last_visible()
            message = f"Selected year is '{new_last_visible_year.text}'"
            new_last_visible_year.click()

        self.log_print("info", message)

        # verify selected year
        selected_year = date_picker_page.get_dt_year_selected().text
        self.verify_in_text(testing_year, selected_year)
        self.driver.refresh()

    @pytest.mark.date_picker
    def test_dt_year_alternative(self, date_picker_page, get_excel_data):
        date_picker_page.get_date_and_time_box().click()

        year_tab = date_picker_page.get_dt_year_tab()  # select year tab
        by_locator = date_picker_page.dt_year_tab
        self.explicitly_wait(by_locator, 5, "presence_of_element_located")
        year_tab.click()
        testing_date = get_excel_data("019_date_and_time_picker", "text_verify")  # testing date from Excel sheet
        testing_year = testing_date.split(" ")[2]  # format Month DD YYYY
        down_arrow = date_picker_page.get_dt_years_scroll_down()  # dynamically calls next year
        i = 0  # to avoid an infinite loop
        while True:
            if i == 100:
                message = f"Too many tries, i = '{i}'"
                self.log_print("error", message)
                break
            try:
                year_element = date_picker_page.get_year_alternative(testing_year)
                if year_element.is_displayed():
                    message = f"{year_element.text} found, clicking."
                    self.log_print("info", message)
                    year_element.click()
                    break
            except NoSuchElementException:
                self.scroll_into_view(down_arrow)
                down_arrow.click()
            i += 1

    @pytest.mark.date_picker
    def test_dt_month(self, date_picker_page, get_excel_data):
        date_picker_page.get_dt_month_tab().click()
        month_options = date_picker_page.get_dt_month_options()
        month_testing = get_excel_data("019_date_and_time_picker", "text_verify").split(" ")[0]

        for month in month_options:
            if month_testing in month.text:
                message = f"Selected mont is '{month.text}'"
                self.log_print("info", message)
                month.click()
                break

        # verify testing month selected
        month_selected = date_picker_page.get_dt_month_selected().text
        self.verify_in_text(month_testing, month_selected)

    @pytest.mark.date_picker
    def test_dt_day(self, date_picker_page, get_excel_data):
        day_options = date_picker_page.get_dt_day_options()
        day_testing = get_excel_data("019_date_and_time_picker", "text_verify").split(" ")[1]

        # delete "0" in front of day to match picker format
        if int(day_testing) < 10:
            day_testing = day_testing[1]

        for day in day_options:
            if day_testing in day.text:
                message = f"Selected day is '{day.text}'"
                self.log_print("info", message)
                day.click()
                break

        # verify testing day selected
        dt_selected = date_picker_page.get_dt_selected().get_attribute('value')  # full date and time selected
        day_selected = dt_selected.split(" ")[1]
        self.verify_in_text(day_testing, day_selected)

    @pytest.mark.date_picker
    def test_dt_time(self, date_picker_page, get_excel_data):
        time_options = date_picker_page.get_dt_time_options()
        time_testing = get_excel_data("019_date_and_time_picker", "text_verify").split(" ")[3]

        for option in time_options:
            if time_testing in option.text:
                message = f"Selected time is '{option.text}'"
                self.log_print("info", message)
                option.click()
                break

        # verify testing time selected
        dt_value_selected = date_picker_page.get_dt_selected().get_attribute('value')  # full date and time selected

        dt_value_original_format = datetime.strptime(dt_value_selected, "%B %d, %Y %I:%M %p")
        # Month, dd, yyyy hh:mm AM/PM

        formatted_value = dt_value_original_format.strftime("%H:%M")  # time formatted into military time

        self.verify_in_text(time_testing, formatted_value)

    @pytest.mark.date_picker
    def test_dt_verify_date_and_time_selected(self, date_picker_page, get_excel_data):
        dt_value_selected = date_picker_page.get_dt_selected().get_attribute('value')  # full date and time selected

        dt_value_original_format = datetime.strptime(dt_value_selected, "%B %d, %Y %I:%M %p")
        # Month, dd, yyyy hh:mm AM/PM
        formatted_value = dt_value_original_format.strftime("%B %d %Y %H:%M")  # formatted as in Excell sheet

        date_time_testing = get_excel_data("019_date_and_time_picker", "text_verify")

        self.verify_equal(date_time_testing, formatted_value)