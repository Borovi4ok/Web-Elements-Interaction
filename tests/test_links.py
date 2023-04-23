import pytest
import time
from WebInteractionDemoQA.data.test_data import TestData
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Suite 7. Test Links
class TestLinks(Assertions, ReusableFunctions):
    @pytest.mark.links
    def test_url_links(self, urls):
        self.driver.get(urls["links"])
        self.verify_url("links")

    @pytest.mark.links
    def test_dynamic_link(self):
        self.driver.find_element(By.ID, "dynamicLink").click()
        all_open_windows = self.driver.window_handles
        self.driver.switch_to.window(all_open_windows[1])
        self.verify_url("https://demoqa.com/")
        self.driver.switch_to.window(all_open_windows[0])

    @pytest.mark.links
    def test_api_call_link(self):
        links_list = self.driver.find_elements(By.XPATH,
                                               "//h5[contains(., 'Following links will send an api "
                                               "call')]/following-sibling::p/a[contains(@href, 'javascript')]")
        previous_status = ""
        for i in range(0, 7):
            # 7 links
            wait = WebDriverWait(self.driver, 10)

            # send an api call
            element = links_list[i]
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            retries = 0
            while True:
                # wait for element with status code to become visible
                status_element = wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//p[@id='linkResponse']/b[1]")))
                respond_status = status_element.text

                # wait for status code to change after click from previous value
                if respond_status != previous_status:
                    self.verify_equal(respond_status, TestData.expected_status_respond[i])
                    previous_status = respond_status
                    break

                # exit loop after 5 retries
                elif retries >= 5:
                    break

                else:
                    # wait for element to update status code
                    time.sleep(0.5)
                    retries += 1
