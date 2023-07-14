import pytest
from WebInteractionDemoQA.page_objects.objects_TS_021_progress_bar import ProgressBar
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
import time
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def progress_bar_page(setup):
    return ProgressBar(setup)


# Suite 21. Test Progress Bar, Page Object Model
class TestProgressBar(Assertions, ReusableFunctions):
    @pytest.mark.progress_bar
    def test_url_progress_bar(self, urls, get_excel_data):
        self.driver.get(urls["progress_bar"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("021_url_progress_bar", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.progress_bar
    def test_start_position(self, progress_bar_page, get_excel_data):
        progress_info = progress_bar_page.get_progress_info()
        style_attribute = progress_info.get_attribute("style")
        progress = int(style_attribute.split(" ")[1].split("%")[0])
        print(f"progress = {progress}")
        expected_progress = get_excel_data("021_start_position", "text_verify")
        self.verify_equal(progress, expected_progress)

    @pytest.mark.progress_bar
    def test_progress(self, progress_bar_page, get_excel_data):
        # retrieve original width of the entire bar
        progress_bar = progress_bar_page.get_progress_bar()
        bar_width = float(progress_bar.size["width"])
        print(f"bar_width initial = {bar_width}")

        # calculate testing checkpoint in pixels
        testing_progress_data = get_excel_data("021_progress", "text_verify")  # in percents
        progress_info = progress_bar_page.get_progress_info()
        check_point = bar_width / 100 * testing_progress_data

        # print info message to verify progress starts from 0
        computed_original_width = self.driver.execute_script("return parseFloat(getComputedStyle(arguments[0]).width);",
                                                             progress_info)
        message = f"Progress starts from '{computed_original_width}'px. filled in."
        self.log_print("info", message)

        # start progress
        start_button = progress_bar_page.get_start_stop_button()
        start_button.click()

        # dynamically wait for check_point
        while True:
            computed_progress_width = self.driver.execute_script(
                "return parseFloat(getComputedStyle(arguments[0]).width);", progress_info)
            if computed_progress_width >= check_point:
                start_button.click()
                print(f"computed_progress_width = {computed_progress_width}")
                break

            #  small delay to avoid excessive checking
            time.sleep(0.5)

        # retrieve progress from 'stile' attribute in percent
        style_attribute = progress_info.get_attribute("style")
        progress_percent = int(style_attribute.split(" ")[1].split("%")[0])

        # retrieve color indicating progress is going on
        computed_color = self.driver.execute_script("return getComputedStyle(arguments[0]).color;", progress_bar)
        expected_color = get_excel_data("021_progress", "text_verify_2")

        # verify progress bar filled in as expected
        tolerance_pixel = 10
        self.verify_with_tolerance(computed_progress_width, check_point, tolerance_pixel)

        # verify value of "style" attribute matches to the progress
        tolerance_percent = 6
        self.verify_with_tolerance(progress_percent, testing_progress_data, tolerance_percent)

        # verify bar is filled in with the expected color
        self.verify_equal(computed_color, expected_color)

    @pytest.mark.progress_bar
    def test_completed(self, progress_bar_page, get_excel_data):
        # retrieve initial width of the entire bar
        progress_bar = progress_bar_page.get_progress_bar()
        full_bar_width = float(progress_bar.size["width"])

        # start/restart progress
        start_button = progress_bar_page.get_start_stop_button()
        start_button.click()

        # reset_button  - appears when progress is complete
        by_locator = progress_bar_page.reset_button
        self.explicitly_wait(by_locator, 15, "presence_of_element_located")
        # wait for reset button (progress completed)

        # verify filed in bar width matches initial full size of the bar
        completed_progress_bar = progress_bar_page.get_completed_progress_bar()
        computed_completed_width = self.driver.execute_script(
            "return parseFloat(getComputedStyle(arguments[0]).width);", completed_progress_bar)
        tolerance = 5
        self.verify_with_tolerance(computed_completed_width, full_bar_width, tolerance)

        # verify progress status from 'stile' attribute in percent is complete
        style_attribute = completed_progress_bar.get_attribute("style")
        actual_progress = int(style_attribute.split(" ")[1].split("%")[0])
        expected_progress = get_excel_data("021_completed", "text_verify")
        self.verify_equal(actual_progress, expected_progress)

        # verify background color (should be changed by green once completed)
        computed_background_color = self.driver.execute_script("return getComputedStyle(arguments[0]).backgroundColor;",
                                                               completed_progress_bar)
        expected_background_color = get_excel_data("021_completed", "text_verify_2")
        self.verify_equal(computed_background_color,  expected_background_color)

    @pytest.mark.progress_bar
    def test_reset(self, progress_bar_page):
        # verify 'reset button' when progress is completed
        message = "Progress is completed"
        self.log_print("info", message)
        reset_button = progress_bar_page.get_reset_button()
        self.verify_is_displayed(reset_button)

        # reset progress
        reset_button.click()

        # verify 'start/stop' button is back and 'reset' button is gone once progress is reset
        message = "Progress is reset"
        self.log_print("info", message)
        by_locator = progress_bar_page.start_stop_button
        self.explicitly_wait(by_locator, 2, "presence_of_element_located")  # wait for start/stop button to be located
        reset_button_locator = progress_bar_page.reset_button
        locator_strategy, locator_value = reset_button_locator  # call from object page
        self.verify_deleted(locator_strategy, locator_value)
