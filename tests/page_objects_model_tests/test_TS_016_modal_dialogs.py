import pytest
from WebInteractionDemoQA.page_objects.objects_TS_016_modal_dialogs import ModalDialogs
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def modal_dialogs_page(setup):
    return ModalDialogs(setup)


# Suite 16. Test Modal Dialogs, Page Object Model
class TestModalDialogs(Assertions, ReusableFunctions):
    @pytest.mark.modal_dialogs
    def test_url_modal_dialogs(self, urls, get_excel_data):
        self.driver.get(urls["modal_dialogs"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("016_url_modal_dialogs", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.modal_dialogs
    def test_small_modal(self, modal_dialogs_page, get_excel_data):
        modal_dialogs_page.get_small_modal_button().click()

        # get list of all open window and switch to the last (modal)
        all_open_windows = self.driver.window_handles
        self.driver.switch_to.window(all_open_windows[-1])

        # get text from modal dialog and verify it
        text_element = modal_dialogs_page.get_small_modal_text()
        text = text_element.text
        expected_text = get_excel_data("016_small_modal", "text_verify")
        self.verify_in_text(expected_text, text)

        # click close button and switch back to the main window
        modal_dialogs_page.get_small_modal_close_button().click()
        self.driver.switch_to.window(all_open_windows[0])

    @pytest.mark.modal_dialogs
    def test_large_modal(self, modal_dialogs_page, get_excel_data):
        modal_dialogs_page.get_large_modal_button().click()

        # get list of all open window and switch to the last (modal)
        all_open_windows = self.driver.window_handles
        self.driver.switch_to.window(all_open_windows[-1])

        # get text from modal dialog and verify it
        text_element = modal_dialogs_page.get_large_modal_text()
        text = text_element.text
        expected_text = get_excel_data("016_large_modal", "text_verify")
        self.verify_in_text(expected_text, text)

        # click close button and switch back to the main window
        modal_dialogs_page.get_large_modal_close_button().click()
        self.driver.switch_to.window(all_open_windows[0])
