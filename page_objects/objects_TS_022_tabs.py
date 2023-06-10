from selenium.webdriver.common.by import By


class Tabs:
    def __init__(self, driver):
        self.driver = driver

    tabs = (By.CSS_SELECTOR, ".nav.nav-tabs a")
    content = (By.CSS_SELECTOR, "div.fade p:nth-child(1)")

    def get_tabs(self):
        return self.driver.find_elements(*Tabs.tabs)

    def get_content(self):
        return self.driver.find_elements(*Tabs.content)
