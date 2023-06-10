from selenium.webdriver.common.by import By


class Menu:
    def __init__(self, driver):
        self.driver = driver

    main_item_1 = (By.LINK_TEXT, "Main Item 1")
    main_item_2 = (By.LINK_TEXT, "Main Item 2")
    sub_items = (By.XPATH, "//a[text()='Main Item 2']/following-sibling::ul//li/a")
    sub_sub_items = (By.XPATH, "//a[text()='Main Item 2']/following-sibling::ul/li/a/following-sibling::ul/li/a")
    main_item_3 = (By.LINK_TEXT, "Main Item 3")

    def get_main_item_1(self):
        return self.driver.find_element(*Menu.main_item_1)

    def get_main_item_2(self):
        return self.driver.find_element(*Menu.main_item_2)

    def get_sub_items(self):
        return self.driver.find_elements(*Menu.sub_items)

    def get_main_item_3(self):
        return self.driver.find_element(*Menu.main_item_3)
