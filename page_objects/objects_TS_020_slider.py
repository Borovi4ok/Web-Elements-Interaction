from selenium.webdriver.common.by import By


class Slider:
    def __init__(self, driver):
        self.driver = driver
    slider_thumb = (By.CSS_SELECTOR, ".range-slider.range-slider--primary")
    slider_style = (By.CSS_SELECTOR, ".range-slider__tooltip.range-slider__tooltip--auto.range-slider__tooltip--bottom")

    def get_slider_thumb(self):
        return self.driver.find_element(*Slider.slider_thumb)

    def get_slider_style(self):
        return self.driver.find_element(*Slider.slider_style)
