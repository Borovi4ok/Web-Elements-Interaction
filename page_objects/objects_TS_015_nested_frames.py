from selenium.webdriver.common.by import By


class NestedFrames:
    def __init__(self, driver):
        self.driver = driver

    parent_frame = (By.CSS_SELECTOR, "iframe#frame1")
    parent_frame_text = (By.TAG_NAME, "body")
    child_frame = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")
    child_frame_text = (By.TAG_NAME, "body")

    def get_parent_frame(self):
        return self.driver.find_element(*NestedFrames.parent_frame)

    def get_parent_frame_text(self):
        return self.driver.find_element(*NestedFrames.parent_frame_text)

    def get_child_frame(self):
        return self.driver.find_element(*NestedFrames.child_frame)

    def get_child_frame_text(self):
        return self.driver.find_element(*NestedFrames.child_frame_text)
