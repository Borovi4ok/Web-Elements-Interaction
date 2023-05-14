from selenium.webdriver.common.by import By
from WebInteractionDemoQA.data.test_data import TestData
import pytest
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions


# Suite 8. Test Broken Links and Images, Classic Model
class TestBrokenLinksImages(Assertions, ReusableFunctions):
    @pytest.mark.broken_links_images
    def test_url_broken_links(self, urls):
        self.driver.get(urls["broken_links"])
        self.verify_url("broken")

    @pytest.mark.broken_links_images
    def test_valid_image(self):
        valid_image = self.driver.find_element(By.XPATH, "//p[text()='Valid image']/following-sibling::img[1]")
        self.verify_is_displayed(valid_image)
        self.verify_image_width(valid_image)

    @pytest.mark.broken_links_images
    def test_broken_image(self):
        broken_image = self.driver.find_element(By.XPATH, "//p[text()='Valid image']/following-sibling::img[2]")
        self.verify_is_displayed(broken_image)
        self.verify_image_width(broken_image)

    @pytest.mark.broken_links_images
    def test_valid_link(self):
        by_locator = (By.CSS_SELECTOR, "a[href='http://demoqa.com']")
        time_wait = 5
        # call custom wait condition in assert_functions, and get a URL of an opened page
        new_url = self.verify_url_change(by_locator, time_wait)

        # verify the URL of the opened page is as expected
        expected_link_url = TestData.expected_link_url
        self.verify_equal(new_url, expected_link_url)
        self.driver.back()

    @pytest.mark.broken_links_images
    def test_broken_link(self):
        by_locator = (By.CSS_SELECTOR, "a[href='http://the-internet.herokuapp.com/status_codes/500']")
        time_wait = 5
        # call custom wait condition in assert_functions, and get a URL of an opened page
        new_url = self.verify_url_change(by_locator, time_wait)

        # verify the URL of the opened page is as expected
        expected_link_url = TestData.expected_link_url
        self.verify_equal(new_url, expected_link_url)