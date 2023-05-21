import pytest
from WebInteractionDemoQA.page_objects.objects_TS_018_auto_complete import AutoComplete
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def auto_complete_page(setup):
    return AutoComplete(setup)


# Suite 18. Test Auto Complete, Page Object Model
class TestAutoComplete(Assertions, ReusableFunctions):
    @pytest.mark.autocomplete
    def test_url_autocomplete(self, urls, get_excel_data):
        self.driver.get(urls["auto_complete"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("018_url_auto_complete", "text_verify")
        print(expected_url)
        self.verify_url(expected_url)

    @pytest.mark.autocomplete
    def test_multiple_colors_field(self, auto_complete_page, get_excel_data):
        # invoke string with multiple color names from Excel sheet
        colors_data_string = get_excel_data("018_multiple_colors_field", "text_verify")

        # split colors_data_string into a list of colors
        colors_data_list = colors_data_string.split()

        colors_input_field = auto_complete_page.get_multiple_colors_input()

        for color in colors_data_list:
            first_character = color[0]
            # send only the first character of each color name to get auto-complete options

            colors_input_field.send_keys(first_character)

            # wait for options to come
            by_locator = auto_complete_page.colors_options
            self.explicitly_wait(by_locator, 5, "presence_of_all_elements_located")

            colors_options = auto_complete_page.get_colors_options()
            for option in colors_options:
                if option.text == color:
                    option.click()
                    break

        # verify all colors selected as per colors_data_list
        selected_elements = auto_complete_page.get_selected_colors()
        selected_colors = [selected.text for selected in selected_elements]
        self.verify_equal(colors_data_list, selected_colors)

    @pytest.mark.autocomplete
    def test_single_color_field(self, auto_complete_page, get_excel_data):
        # invoke color name from Excel sheet
        color_data_name = get_excel_data("018_single_color_field", "text_verify")
        input_field = auto_complete_page.get_single_colors_input()

        first_characters = color_data_name[0:2]
        # send only the first two characters of color name to get auto-complete options
        print(first_characters)

        input_field.send_keys(first_characters)

        # wait for options to come
        by_locator = auto_complete_page.colors_options
        self.explicitly_wait(by_locator, 5, "presence_of_all_elements_located")

        colors_options = auto_complete_page.get_colors_options()
        for option in colors_options:
            if option.text == color_data_name:
                option.click()
                break

        # verify color selected as per color_data_name
        selected_element = auto_complete_page.get_selected_color()
        selected_color = selected_element.text
        self.verify_equal(color_data_name, selected_color)


