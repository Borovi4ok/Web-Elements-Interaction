from selenium.webdriver.common.by import By


class SelectMenu:
    def __init__(self, driver):
        self.driver = driver

    select_value_dropdown = (By.XPATH, "(//div[contains(@class, 'indicatorContainer')])[1]")
    select_value_items = (By.XPATH, "//*[contains(@id, 'react-select-2-option')]")
    selected_value = (By.CSS_SELECTOR, '.css-1uccc91-singleValue')
    select_one_dropdown = (By.XPATH, "(//div[contains(@class, 'indicatorContainer')])[2]")
    select_one_items = (By.XPATH, "//*[contains(@id, 'react-select-3-option')]")
    selected_one_value = (By.XPATH, "(//div[@class=' css-1uccc91-singleValue'])[last()]")
    old_style_menu_dropdown = (By.ID, "oldSelectMenu")
    old_style_menu_items = (By.CSS_SELECTOR, "#oldSelectMenu option")
    multiselect_dropdown_arrow = (By.XPATH, "(//div[contains(@class, 'indicatorContainer')])[3]")
    multiselect_dropdown_items = (By.XPATH, "//*[contains(@id, 'react-select-4-option')]")
    multiselect_dropdown_selected_items = (By.CLASS_NAME, "css-12jo7m5")
    multiselect_dropdown_delete_one = (By.CSS_SELECTOR, "div.css-1rhbuit-multiValue div:nth-child(2)")
    multiselect_dropdown_delete_all = (By.CSS_SELECTOR, ".css-1gtu0rj-indicatorContainer:nth-of-type(1)")

    def get_select_value_dropdown(self):
        return self.driver.find_element(*SelectMenu.select_value_dropdown)

    def get_select_value_items(self):
        return self.driver.find_elements(*SelectMenu.select_value_items)

    def get_selected_value(self):
        return self.driver.find_element(*SelectMenu.selected_value)

    def get_select_one_dropdown(self):
        return self.driver.find_element(*SelectMenu.select_one_dropdown)

    def get_select_one_items(self):
        return self.driver.find_elements(*SelectMenu.select_one_items)

    def get_selected_one_value(self):
        return self.driver.find_element(*SelectMenu.selected_one_value)

    def get_old_style_menu_dropdown(self):
        return self.driver.find_element(*SelectMenu.old_style_menu_dropdown)

    def get_old_style_menu_items(self):
        return self.driver.find_elements(*SelectMenu.old_style_menu_items)

    def get_multiselect_dropdown_arrow(self):
        return self.driver.find_element(*SelectMenu.multiselect_dropdown_arrow)

    def get_multiselect_dropdown_items(self):
        return self.driver.find_elements(*SelectMenu.multiselect_dropdown_items)

    def get_multiselect_dropdown_selected_items(self):
        return self.driver.find_elements(*SelectMenu.multiselect_dropdown_selected_items)

    def get_multiselect_dropdown_delete_one(self):
        return self.driver.find_elements(*SelectMenu.multiselect_dropdown_delete_one)

    def get_multiselect_dropdown_delete_all(self):
        return self.driver.find_element(*SelectMenu.multiselect_dropdown_delete_all)
