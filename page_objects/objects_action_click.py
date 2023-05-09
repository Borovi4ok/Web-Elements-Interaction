from selenium.webdriver.common.by import By


class ObjectsActionClick:
    def __init__(self, driver):
        self.driver = driver

    double_click_button = (By.ID, "doubleClickBtn")
    double_click_message = (By.ID, "doubleClickMessage")
    right_click_button = (By.ID, "rightClickBtn")
    right_click_message = (By.ID, "rightClickMessage")
    dynamic_click_button = (By.XPATH, "//button[@type='button' and text()='Click Me']")
    dynamic_click_message = (By.ID, "dynamicClickMessage")

    def get_double_click_button(self):
        return self.driver.find_element(*ObjectsActionClick.double_click_button)

    def get_double_click_message(self):
        return self.driver.find_element(*ObjectsActionClick.double_click_message)

    def get_right_click_button(self):
        return self.driver.find_element(*ObjectsActionClick.right_click_button)

    def get_right_click_message(self):
        return self.driver.find_element(*ObjectsActionClick.right_click_message)

    def get_dynamic_click_button(self):
        return self.driver.find_element(*ObjectsActionClick.dynamic_click_button)

    def get_dynamic_click_message(self):
        return self.driver.find_element(*ObjectsActionClick.dynamic_click_message)
