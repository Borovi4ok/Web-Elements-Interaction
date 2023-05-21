from selenium.webdriver.common.by import By


class AutoComplete:
    def __init__(self, driver):
        self.driver = driver

    multiple_colors_input = (By.ID, "autoCompleteMultipleInput")
    colors_options = (By.CSS_SELECTOR, ".auto-complete__option")
    selected_colors = (By.CSS_SELECTOR, ".auto-complete__multi-value__label")
    single_colors_input = (By.ID, "autoCompleteSingleInput")
    selected_color = (By.CSS_SELECTOR, ".auto-complete__single-value")

    def get_multiple_colors_input(self):
        return self.driver.find_element(*AutoComplete.multiple_colors_input)

    def get_colors_options(self):
        return self.driver.find_elements(*AutoComplete.colors_options)

    def get_selected_colors(self):
        return self.driver.find_elements(*AutoComplete.selected_colors)

    def get_single_colors_input(self):
        return self.driver.find_element(*AutoComplete.single_colors_input)

    def get_selected_color(self):
        return self.driver.find_element(*AutoComplete.selected_color)
