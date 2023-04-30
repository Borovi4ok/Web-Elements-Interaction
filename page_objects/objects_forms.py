from selenium.webdriver.common.by import By


class ObjectsForms:
    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.CSS_SELECTOR, "input#userEmail")
    gender_radio_click = (By.XPATH, "//div[@class='custom-control custom-radio custom-control-inline']")

    # chained locator
    gender_radio_label = (By.XPATH, ".//label")
    gender_radio_assert = (By.XPATH, "//input[@type='radio']")
    mobile = (By.CSS_SELECTOR, "input#userNumber")
    calendar_dropdown = (By.ID, "dateOfBirthInput")
    calendar_month_dropdown = (By.XPATH, "//div[@class='react-datepicker__month-dropdown-container "
                                         "react-datepicker__month-dropdown-container--select']")
    calendar_month_options = (By.XPATH, "//div[@class='react-datepicker__month-dropdown-container "
                                        "react-datepicker__month-dropdown-container--select']//option")
    calendar_year_dropdown = (By.XPATH, "//div[@class='react-datepicker__year-dropdown-container "
                                        "react-datepicker__year-dropdown-container--select']")
    calendar_year_options = (By.XPATH, "//div[@class='react-datepicker__year-dropdown-container "
                                       "react-datepicker__year-dropdown-container--select']//option")
    calendar_day_options = (By.XPATH, "//div[@class='react-datepicker__week']//div")
    subjects_auto_complete_field = (By.CSS_SELECTOR, "input#subjectsInput")
    subjects_auto_complete_suggestions = (By.CSS_SELECTOR, "div.subjects-auto-complete__option.css-yt9ioa-option")
    subjects_auto_complete_result = (By.CSS_SELECTOR, "div.css-12jo7m5.subjects-auto-complete__multi-value__label")
    hobbies_check_boxes_clickable = (By.XPATH, "//div[@class='custom-control custom-checkbox custom-control-inline']")
    hobbies_check_boxes_assertable = (By.XPATH, "//input[@type='checkbox']")
    picture_upload = (By.CSS_SELECTOR, "input#uploadPicture")
    address_text_area = (By.CSS_SELECTOR, "textarea#currentAddress")
    state_dropdown = (By.XPATH, "(//div[@class=' css-tlfecz-indicatorContainer'])[1]")
    state_options = (By.XPATH, "//div[@class=' css-yt9ioa-option' or @class=' css-1n7v3ny-option']")
    state_selected = (By.CLASS_NAME, "css-1uccc91-singleValue")
    city_dropdown = (By.XPATH, "( //div[@class=' css-1wy0on6'])[2]")
    city_options = (By.XPATH, "//div[@class=' css-1n7v3ny-option' or @class=' css-yt9ioa-option']")
    city_selected = (By.XPATH, "(//div[@class=' css-1uccc91-singleValue'])[2]")
    submit_button = (By.CSS_SELECTOR, "button#submit")
    success_message = (By.ID, "example-modal-sizes-title-lg")
    confirmation_table = (By.XPATH, "//div[@class='table-responsive']//td")

    def get_first_name(self):
        return self.driver.find_element(*ObjectsForms.first_name)

    def get_last_name(self):
        return self.driver.find_element(*ObjectsForms.last_name)

    def get_email(self):
        return self.driver.find_element(*ObjectsForms.email)

    def get_gender_radio_click(self):
        return self.driver.find_elements(*ObjectsForms.gender_radio_click)

    @staticmethod
    # returns chained locator from "get_gender_radio_click"
    def get_gender_radio_label(parent_element):
        return parent_element.find_element(*ObjectsForms.gender_radio_label)

    def get_gender_radio_assert(self):
        return self.driver.find_elements(*ObjectsForms.gender_radio_assert)

    def get_mobile(self):
        return self.driver.find_element(*ObjectsForms.mobile)

    def get_calendar_dropdown(self):
        return self.driver.find_element(*ObjectsForms.calendar_dropdown)

    def get_calendar_month_dropdown(self):
        return self.driver.find_element(*ObjectsForms.calendar_month_dropdown)

    def get_calendar_month_options(self):
        return self.driver.find_elements(*ObjectsForms.calendar_month_options)

    def get_calendar_year_dropdown(self):
        return self.driver.find_element(*ObjectsForms.calendar_year_dropdown)

    def get_calendar_year_options(self):
        return self.driver.find_elements(*ObjectsForms.calendar_year_options)

    def get_calendar_day_options(self):
        return self.driver.find_elements(*ObjectsForms.calendar_day_options)

    def get_subjects_auto_complete_field(self):
        return self.driver.find_element(*ObjectsForms.subjects_auto_complete_field)

    def get_subjects_auto_complete_suggestions(self):
        return self.driver.find_elements(*ObjectsForms.subjects_auto_complete_suggestions)

    def get_subjects_auto_complete_result(self):
        return self.driver.find_elements(*ObjectsForms.subjects_auto_complete_result)

    def get_hobbies_check_boxes_clickable(self):
        return self.driver.find_elements(*ObjectsForms.hobbies_check_boxes_clickable)

    def get_hobbies_check_boxes_assertable(self):
        return self.driver.find_elements(*ObjectsForms.hobbies_check_boxes_assertable)

    def get_picture_upload(self):
        return self.driver.find_element(*ObjectsForms.picture_upload)

    def get_address_text_area(self):
        return self.driver.find_element(*ObjectsForms.address_text_area)

    def get_state_dropdown(self):
        return self.driver.find_element(*ObjectsForms.state_dropdown)

    def get_state_options(self):
        return self.driver.find_elements(*ObjectsForms.state_options)

    def get_state_selected(self):
        return self.driver.find_elements(*ObjectsForms.state_selected)

    def get_city_dropdown(self):
        return self.driver.find_element(*ObjectsForms.city_dropdown)

    def get_city_options(self):
        return self.driver.find_elements(*ObjectsForms.city_options)

    def get_city_selected(self):
        return self.driver.find_elements(*ObjectsForms.city_selected)

    def get_submit_button(self):
        return self.driver.find_element(*ObjectsForms.submit_button)

    def get_success_message(self):
        return self.driver.find_element(*ObjectsForms.success_message)

    def get_confirmation(self):
        return self.driver.find_elements(*ObjectsForms.confirmation_table)
