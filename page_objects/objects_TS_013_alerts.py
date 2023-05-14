from selenium.webdriver.common.by import By


class Alerts:
    def __init__(self, driver):
        self.driver = driver

    alert_button = (By.XPATH, "//button[@id='alertButton']")
    delayed_alert_button = (By.ID, "timerAlertButton")
    confirm_button = (By.ID, "confirmButton")
    confirm_result_message = (By.ID, "confirmResult")
    prompt_button = (By.ID, "promtButton")
    prompt_result_message = (By.ID, "promptResult")

    def get_alert_button(self):
        return self.driver.find_element(*Alerts.alert_button)

    def get_delayed_alert_button(self):
        return self.driver.find_element(*Alerts.delayed_alert_button)

    def get_confirm_button(self):
        return self.driver.find_element(*Alerts.confirm_button)

    def get_confirm_result_message(self):
        return self.driver.find_element(*Alerts.confirm_result_message)

    def get_prompt_button(self):
        return self.driver.find_element(*Alerts.prompt_button)

    def get_prompt_result_message(self):
        return self.driver.find_element(*Alerts.prompt_result_message)
