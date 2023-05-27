from selenium.webdriver.common.by import By


class DatePicker:
    def __init__(self, driver):
        self.driver = driver

    date_box = (By.ID, "datePickerMonthYearInput")
    year_select = (By.CSS_SELECTOR, ".react-datepicker__year-select option")
    months_select = (By.CSS_SELECTOR, ".react-datepicker__month-select option")
    day_picker = (By.XPATH, "//div[@class='react-datepicker__week']/div[not(contains(@class, '--outside-month'))]/a")
    date_and_time_box = (By.ID, "dateAndTimePickerInput")
    year_tab = (By.CLASS_NAME, "react-datepicker__year-read-view--down-arrow")
    year_options = (By.XPATH, "//div[contains(@class, 'react-datepicker__year-option')]")
    years_scroll_down = (By.XPATH, "//div[@class='react-datepicker__year-option'][last()]")
    last_visible_year = (By.XPATH, "//div[@class='react-datepicker__year-option'][last()-1]")

    def get_date_box(self):
        return self.driver.find_element(*DatePicker.date_box)

    def get_years(self):
        return self.driver.find_elements(*DatePicker.year_select)

    def get_months(self):
        return self.driver.find_elements(*DatePicker.months_select)

    def get_days(self):
        return self.driver.find_elements(*DatePicker.day_picker)

    def get_date_and_time_box(self):
        return self.driver.find_element(*DatePicker.date_and_time_box)

    def get_year_tab(self):
        return self.driver.find_element(*DatePicker.year_tab)

    def get_year_options(self):
        return self.driver.find_elements(*DatePicker.year_options)

    def get_years_scroll_down(self):
        return self.driver.find_element(*DatePicker.years_scroll_down)

    def get_last_visible_year(self):
        return self.driver.find_element(*DatePicker.last_visible_year)
