import pytest
from WebInteractionDemoQA.page_objects.objects_browser_windows import BrowserWindows
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def windows_page(setup):
    return BrowserWindows(setup)


# Suite 12. Test Browser Windows, Page Object Model
class TestWindows(Assertions, ReusableFunctions):
    @pytest.mark.windows
    def test_url_windows(self, urls, get_excel_data):
        self.driver.get(urls["windows"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("011_url_windows", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.windows
    def test_new_tab(self, windows_page, get_excel_data):
        windows_page.get_new_tab_button().click()
        all_open_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_open_tabs[1])

        # verify URL of a new tab
        expected_url = get_excel_data("011_new_tab", "url_verify")
        self.verify_url(expected_url)

        # verify success message in a new tab
        self.explicitly_wait_for_element(windows_page.new_tab_message, 5, "presence_of_element_located")
        actual_success_message = windows_page.get_new_tab_message().text
        expected_success_message = get_excel_data("011_new_tab", "text_verify")
        self.verify_equal(actual_success_message, expected_success_message)

        # close an extra tab and switch focus back to the original tab
        self.driver.close()
        self.driver.switch_to.window(all_open_tabs[0])

    @pytest.mark.windows
    def test_new_window(self, windows_page, get_excel_data):
        windows_page.get_new_window_button().click()
        all_open_windows = self.driver.window_handles
        self.driver.switch_to.window(all_open_windows[1])

        # verify URL of a new window
        expected_url = get_excel_data("011_new_tab", "url_verify")
        self.verify_url(expected_url)

        # verify success message in a new window
        self.explicitly_wait_for_element(windows_page.new_window_message, 5, "presence_of_element_located")
        actual_success_message = windows_page.get_new_window_message().text
        expected_success_message = get_excel_data("011_new_tab", "text_verify")
        self.verify_equal(actual_success_message, expected_success_message)

        # close an extra window and switch focus back to the original window
        self.driver.close()
        self.driver.switch_to.window(all_open_windows[0])

    @pytest.mark.windows
    def test_about_blank_window(self, windows_page, get_excel_data):
        windows_page.get_about_blank_button().click()
        all_open_windows = self.driver.window_handles
        self.driver.switch_to.window(all_open_windows[-1])

        # verify text in a new about:blank window
        self.explicitly_wait_for_element(windows_page.new_about_blank_message, 5, "presence_of_element_located")
        actual_text = windows_page.get_about_blank_message().text
        expected_text = get_excel_data("011_about_blank_window", "text_verify")
        self.verify_in_text(expected_text, actual_text)

        # close an extra window and switch focus back to the original window
        self.driver.close()
        self.driver.switch_to.window(all_open_windows[0])
