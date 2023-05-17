from selenium.webdriver.common.by import By


class Frames:
    def __init__(self, driver):
        self.driver = driver

    iframe_1 = (By.CSS_SELECTOR, "iframe#frame1")
    text_iframe_1 = (By.XPATH, "//h1[@id='sampleHeading']")

    # an alternative way switch to iframe
    iframes = (By.XPATH, "//iframe[@src='/sample']")

    text_iframe_2 = (By.XPATH, "//h1[@id='sampleHeading']")

    def get_iframe_1(self):
        return self.driver.find_element(*Frames.iframe_1)

    def get_text_iframe_1(self):
        return self.driver.find_element(*Frames.text_iframe_1)

    # get list of iframes
    def get_iframes(self):
        return self.driver.find_elements(*Frames.iframes)

    def get_text_iframe_2(self):
        return self.driver.find_element(*Frames.text_iframe_2)
