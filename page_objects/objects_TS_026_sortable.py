from selenium.webdriver.common.by import By


class Sortable:
    def __init__(self, driver):
        self.driver = driver

    list_items = (By.XPATH, "//div[@class='vertical-list-container mt-4']/div")
    grid_tab = (By.CSS_SELECTOR, "a#demo-tab-grid")
    grid_items = (By.XPATH, "//div[@class='create-grid']/div")

    def get_list_items(self):
        return self.driver.find_elements(*Sortable.list_items)

    def get_grid_tab(self):
        return self.driver.find_element(*Sortable.grid_tab)

    def get_grid_items(self):
        return self.driver.find_elements(*Sortable.grid_items)