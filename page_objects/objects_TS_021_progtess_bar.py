from selenium.webdriver.common.by import By


class ProgressBar:
    def __init__(self, driver):
        self.driver = driver

    progress_info = (By.CSS_SELECTOR, ".bg-info")
    start_stop_button = (By.ID, "startStopButton")
    progress_bar = (By.CSS_SELECTOR, "#progressBar.progress")
    reset_button = (By.CSS_SELECTOR, "#resetButton")
    completed_progress_bar = (By.CSS_SELECTOR, ".progress-bar.bg-success")

    def get_progress_info(self):
        return self.driver.find_element(*ProgressBar.progress_info)

    def get_start_stop_button(self):
        return self.driver.find_element(*ProgressBar.start_stop_button)

    def get_progress_bar(self):
        return self.driver.find_element(*ProgressBar.progress_bar)

    def get_reset_button(self):
        return self.driver.find_element(*ProgressBar.reset_button)

    def get_completed_progress_bar(self):
        return self.driver.find_element(*ProgressBar.completed_progress_bar)