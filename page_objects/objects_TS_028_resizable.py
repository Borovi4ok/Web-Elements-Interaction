from selenium.webdriver.common.by import By


class Resizable:
    def __init__(self, driver):
        self.driver = driver

    restricted_box = (By.ID, "resizableBoxWithRestriction")
    react_resizable_handle = (By.XPATH, "(//span[@class='react-resizable-handle react-resizable-handle-se'])[1] ")
    constraint_area = (By.CLASS_NAME, "constraint-area")
    unrestricted_box = (By.ID, "resizable")

    def get_restricted_box(self):
        return self.driver.find_element(*Resizable.restricted_box)

    def get_react_resizable_handle(self):
        return self.driver.find_element(*Resizable.react_resizable_handle)

    def get_constraint_area(self):
        return self.driver.find_element(*Resizable.constraint_area)

    def get_unrestricted_box(self):
        return self.driver.find_element(*Resizable.unrestricted_box)
