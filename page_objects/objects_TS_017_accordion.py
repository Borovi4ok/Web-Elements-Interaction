from selenium.webdriver.common.by import By


class Accordion:
    def __init__(self, driver):
        self.driver = driver

    card_headers = (By.CLASS_NAME, "card-header")

    # chaining from "card_headers"
    toggle_indicator = (By.XPATH, "./following-sibling::div")

    # chaining from "card_headers"
    card_context = (By.XPATH, "./following-sibling::div//p")

    def get_card_headers(self):
        return self.driver.find_elements(*Accordion.card_headers)

    @staticmethod
    # returns chained element from "card_headers"
    def get_toggle_indicator(parent_element):
        return parent_element.find_element(*Accordion.toggle_indicator)

    @staticmethod
    # returns chained element from "card_headers"
    def get_card_context(parent_element):
        return parent_element.find_element(*Accordion.card_context)