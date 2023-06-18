from selenium.webdriver.common.by import By


class Selectable:
    def __init__(self, driver):
        self.driver = driver

    list_items = (By.XPATH, "//ul[@id='verticalListContainer']/li")
    grid_tab = (By.CSS_SELECTOR, "a#demo-tab-grid")
    grid_items = (By.XPATH, "//div[@class='list-group list-group-horizontal-sm']/li")

    def get_list_items(self):
        return self.driver.find_elements(*Selectable.list_items)

    def get_grid_tab(self):
        return self.driver.find_element(*Selectable.grid_tab)

    def get_grid_items(self):
        return self.driver.find_elements(*Selectable.grid_items)