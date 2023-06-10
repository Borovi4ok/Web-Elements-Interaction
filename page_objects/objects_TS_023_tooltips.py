from selenium.webdriver.common.by import By


class Tooltips:
    def __init__(self, driver):
        self.driver = driver

    button = (By.ID, "toolTipButton")
    text_field = (By.ID, "toolTipTextField")
    link = (By.LINK_TEXT, "Contrary")
    hover = (By.CLASS_NAME, "tooltip-inner")

    def get_button(self):
        return self.driver.find_element(*Tooltips.button)

    def get_text_field(self):
        return self.driver.find_element(*Tooltips.text_field)

    def get_link(self):
        return self.driver.find_element(*Tooltips.link)

