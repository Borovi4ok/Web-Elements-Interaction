from selenium.webdriver.common.by import By


class DatePicker:
    def __init__(self, driver):
        self.driver = driver

    date_box = (By.ID, "datePickerMonthYearInput")
    year_select = (By.CSS_SELECTOR, ".react-datepicker__year-select option")
    year_select_alternative = "//div[@class='react-datepicker__year-option' and text()='{}']"
    # accepts text as an argument of get_year_select_alternative to replace placeholder{}

    months_select = (By.CSS_SELECTOR, ".react-datepicker__month-select option")
    day_picker = (By.XPATH, "//div[@class='react-datepicker__week']/div[not(contains(@class, '--outside-month'))]")
    date_and_time_box = (By.ID, "dateAndTimePickerInput")  # dt = date & time picker
    dt_year_tab = (By.CLASS_NAME, "react-datepicker__year-read-view--down-arrow")
    dt_year_options = (By.XPATH, "//div[contains(@class, 'react-datepicker__year-option')]")
    dt_years_scroll_down = (By.XPATH, "//div[@class='react-datepicker__year-option'][last()]")
    dt_year_last_visible = (By.XPATH, "//div[@class='react-datepicker__year-option'][last()-1]")
    dt_year_selected = (By.CLASS_NAME, "react-datepicker__year-read-view--selected-year")
    dt_month_tab = (By.CLASS_NAME, "react-datepicker__month-read-view--down-arrow")
    dt_month_options = (By.XPATH, "//div[contains(@class, 'react-datepicker__month-option')]")
    dt_month_selected = (By.CLASS_NAME, "react-datepicker__month-read-view--selected-month")
    dt_day_options = (By.XPATH, "//div[contains(@class, 'react-datepicker__day react-datepicker__day') and not(contains(@class, '--outside-month'))]")
    dt_selected = (By.ID, "dateAndTimePickerInput")
    dt_time_options = (By.CLASS_NAME, "react-datepicker__time-list-item ")

    def get_date_box(self):
        return self.driver.find_element(*DatePicker.date_box)

    def get_years(self):
        return self.driver.find_elements(*DatePicker.year_select)

    def get_year_alternative(self, year):
        xpath = self.year_select_alternative.format(year)
        # accepts year to replace placeholder{} in DatePicker.year_select_alternative locator
        return self.driver.find_element(By.XPATH, xpath)

    def get_months(self):
        return self.driver.find_elements(*DatePicker.months_select)

    def get_days(self):
        return self.driver.find_elements(*DatePicker.day_picker)

    def get_date_and_time_box(self):
        return self.driver.find_element(*DatePicker.date_and_time_box)

    def get_dt_year_tab(self):
        return self.driver.find_element(*DatePicker.dt_year_tab)

    def get_dt_year_options(self):
        return self.driver.find_elements(*DatePicker.dt_year_options)

    def get_dt_years_scroll_down(self):
        return self.driver.find_element(*DatePicker.dt_years_scroll_down)

    def get_dt_year_last_visible(self):
        return self.driver.find_element(*DatePicker.dt_year_last_visible)

    def get_dt_year_selected(self):
        return self.driver.find_element(*DatePicker.dt_year_selected)

    def get_dt_month_tab(self):
        return self.driver.find_element(*DatePicker.dt_month_tab)

    def get_dt_month_options(self):
        return self.driver.find_elements(*DatePicker.dt_month_options)

    def get_dt_month_selected(self):
        return self.driver.find_element(*DatePicker.dt_month_selected)

    def get_dt_day_options(self):
        return self.driver.find_elements(*DatePicker.dt_day_options)

    def get_dt_selected(self):
        return self.driver.find_element(*DatePicker.dt_selected)

    def get_dt_time_options(self):
        return self.driver.find_elements(*DatePicker.dt_time_options)
