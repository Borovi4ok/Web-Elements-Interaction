from selenium.webdriver.common.by import By


class ModalDialogs:
    def __init__(self, driver):
        self.driver = driver

    small_modal_button = (By.ID, "showSmallModal")
    small_modal_text = (By.CSS_SELECTOR, "div[class=modal-body]")
    small_modal_close_button = (By.ID, "closeSmallModal")
    large_modal_button = (By.ID, "showLargeModal")
    large_modal_text = (By.XPATH, "//div[@class='modal-body']/p")
    large_modal_close_button = (By.ID, "closeLargeModal")

    def get_small_modal_button(self):
        return self.driver.find_element(*ModalDialogs.small_modal_button)

    def get_small_modal_text(self):
        return self.driver.find_element(*ModalDialogs.small_modal_text)

    def get_small_modal_close_button(self):
        return self.driver.find_element(*ModalDialogs.small_modal_close_button)

    def get_large_modal_button(self):
        return self.driver.find_element(*ModalDialogs.large_modal_button)

    def get_large_modal_text(self):
        return self.driver.find_element(*ModalDialogs.large_modal_text)

    def get_large_modal_close_button(self):
        return self.driver.find_element(*ModalDialogs.large_modal_close_button)
