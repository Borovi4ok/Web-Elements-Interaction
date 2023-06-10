import pytest
from selenium.webdriver.common.action_chains import ActionChains
from WebInteractionDemoQA.page_objects.objects_TS_023_tooltips import Tooltips
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
import time
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def tooltips_page(setup):
    return Tooltips(setup)


@pytest.fixture
def actions(setup):
    return ActionChains(setup)


# Suite 23. Test Tooltips, Page Object Model
class TestTooltips(Assertions, ReusableFunctions):
    @pytest.mark.tooltips
    def test_url_tooltips(self, urls, get_excel_data):
        self.driver.get(urls["tooltips"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("023_url_tooltips", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.tooltips
    def test_button_hover(self, tooltips_page, actions):
        button = tooltips_page.get_button()
        actions.move_to_element(button).perform()

        # locate tooltip and verify text is displayed
        by_locator = tooltips_page.hover
        hover = self.explicitly_wait(by_locator, 5, "visibility_of_element_located")
        message = f"Tooltip text is '{hover.text}'"
        self.log_print("info", message)
        self.verify_is_displayed(hover)

    @pytest.mark.tooltips
    def test_text_field_hover(self, tooltips_page, actions):
        text_field = tooltips_page.get_text_field()
        actions.move_to_element(text_field).perform()

        # wait for previous tooltip to becomes stale
        time.sleep(1)

        # locate tooltip and verify text is displayed
        by_locator = tooltips_page.hover
        hover = self.explicitly_wait(by_locator, 5, "visibility_of_element_located")
        message = f"Tooltip text is '{hover.text}'"
        self.log_print("info", message)
        self.verify_is_displayed(hover)

    @pytest.mark.tooltips
    def test_text_link(self, tooltips_page, actions):
        link = tooltips_page.get_link()
        actions.move_to_element(link).perform()

        # wait for previous tooltip to becomes stale
        time.sleep(1)

        # locate tooltip and verify text is displayed
        by_locator = tooltips_page.hover
        hover = self.explicitly_wait(by_locator, 5, "visibility_of_element_located")
        message = f"Tooltip text is '{hover.text}'"
        self.log_print("info", message)
        self.verify_is_displayed(hover)
