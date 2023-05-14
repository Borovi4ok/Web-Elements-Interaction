from selenium.webdriver.common.by import By


class BrowserWindows:
    def __init__(self, driver):
        self.driver = driver

    new_tab_button = (By.CSS_SELECTOR, "button#tabButton")
    new_tab_message = (By.CSS_SELECTOR, "h1#sampleHeading")
    new_window_button = (By.CSS_SELECTOR, "button#windowButton")
    new_window_message = (By.CSS_SELECTOR, "h1#sampleHeading")
    new_about_blank_button = (By.CSS_SELECTOR, "button#messageWindowButton")
    new_about_blank_message = (By.TAG_NAME, "body")

    def get_new_tab_button(self):
        return self.driver.find_element(*BrowserWindows.new_tab_button)

    def get_new_tab_message(self):
        return self.driver.find_element(*BrowserWindows.new_tab_message)

    def get_new_window_button(self):
        return self.driver.find_element(*BrowserWindows.new_window_button)

    def get_new_window_message(self):
        return self.driver.find_element(*BrowserWindows.new_window_message)

    def get_about_blank_button(self):
        return self.driver.find_element(*BrowserWindows.new_about_blank_button)

    def get_about_blank_message(self):
        return self.driver.find_element(*BrowserWindows.new_about_blank_message)
