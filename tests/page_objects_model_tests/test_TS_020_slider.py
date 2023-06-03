import pytest
from selenium.webdriver.common.action_chains import ActionChains
from WebInteractionDemoQA.page_objects.objects_TS_020_slider import Slider
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def slider_page(setup):
    return Slider(setup)


# Suite 20. Test Slider, Page Object Model
class TestSlider(Assertions, ReusableFunctions):
    @pytest.mark.slider
    def test_url_slider(self, urls, get_excel_data):
        self.driver.get(urls["slider"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("020_url_slider", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.slider
    def test_thumb_original_position(self, slider_page, get_excel_data):
        slider_thumb = slider_page.get_slider_thumb()
        original_value = slider_thumb.get_attribute("value")
        expected_value = get_excel_data("020_thumb_original_position", "text_verify")
        message = f"Slider thumb original value is '{original_value}'"
        self.log_print("info", message)
        self.verify_equal(int(original_value), expected_value)

    @pytest.mark.slider
    def test_slider(self, slider_page, get_excel_data):
        action = ActionChains(self.driver)
        slider_thumb = slider_page.get_slider_thumb()

        # element contains 'style' attribute with dynamic calculation of slider percentage
        slider_range = slider_page.get_slider_style()
        style = slider_range.get_attribute("style")
        percentage = int(style.split("(")[1].split("%")[0])
        # original position of the thumb against the entire slider in percent

        coefficient = 100 / percentage
        # represents ratio of the initial position of the thumb to the maximum possible value of the slider

        slider_size = slider_thumb.size
        slider_x_size = int(slider_size['width'])  # in pixels
        thumb_x_position = slider_x_size / coefficient
        # original position of the thumb from the left side of the slider in pixels

        pixel_value_ratio = slider_x_size / 100
        # number of pixels needed to add 1 value unit to the slider

        offsets_str = get_excel_data("020_slider", "text_verify")
        offsets = [int(offset) for offset in offsets_str.split() if offset.strip()]

        start_position = slider_x_size / 2
        # the slider implementation assumes drag_and_drop_by_offset() method always starts from the middle

        for offset in offsets:
            message = f"Drag offset is '{offset}'"
            self.log_print("info", message)
            action.drag_and_drop_by_offset(slider_thumb, offset, 0).perform()

            # calculate expected slider value
            math_slider_value = (start_position + offset) / pixel_value_ratio  # in slider's value units
            expected_slider_value = round(math_slider_value, 2)
            if offset + start_position > slider_x_size:
                expected_slider_value = 100

            elif offset + start_position < 0:
                expected_slider_value = 0

            # extract new actual value
            value = slider_thumb.get_attribute("value")
            actual_slider_value = float(value)

            tolerance = 2
            self.verify_with_tolerance(actual_slider_value, expected_slider_value, tolerance)