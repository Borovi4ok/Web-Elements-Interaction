from selenium.webdriver.support.ui import WebDriverWait
from WebInteractionDemoQA.page_objects.objects_TS_017_accordion import Accordion
import pytest
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def accordion_page(setup):
    return Accordion(setup)


# Suite 17. Test Accordion, Page Object Model
class TestAccordion(Assertions, ReusableFunctions):
    @pytest.mark.accordion
    def test_url_accordion(self, urls, get_excel_data):
        self.driver.get(urls["accordion"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("017_url_accordion", "text_verify")
        print(expected_url)
        self.verify_url(expected_url)

    @pytest.mark.accordion
    def test_accordion(self, accordion_page, get_excel_data):
        accordion_card_headers = accordion_page.get_card_headers()
        list_length = len(accordion_card_headers)

        # include message with card headers number in log
        log_message = f"Found {list_length} card headers in accordion"
        log_level = "info"
        self.log_print(log_level, log_message)

        # retriv accordion toggle indicator (class) values from Excel data sheet
        collapsed_card_indicator = get_excel_data("017_accordion_collapsed", "attribute_value")
        expanded_card_indicator = get_excel_data("017_accordion_expanded", "attribute_value")

        for element in accordion_card_headers:
            # indicate card header name in log
            card_header = element.text
            log_message = f"Testing '{card_header}' card:"
            log_level = "info"
            self.log_print(log_level, log_message)

            # chaining from card header to verify card toggle indicator
            toggle_indicator = accordion_page.get_toggle_indicator(element)

            # get attribute to define if card is collapsed or expanded
            toggle_indicator_status = toggle_indicator.get_attribute("class")

            # if accordion card is collapsed - expand(click), if status is "collapse show" - do nothing
            if toggle_indicator_status == collapsed_card_indicator:
                self.scroll_into_view(element)
                element.click()

            # call "attribute_contains" reusable function to use custom wait with E.C. "attribute_contains"
            WebDriverWait(self.driver, 5).until(self.attribute_contains(toggle_indicator, "class", expanded_card_indicator))

            # verify toggle indicator has changed to "collapse show" (expanded)
            toggle_indicator_status = toggle_indicator.get_attribute("class")
            self.verify_equal(toggle_indicator_status, expanded_card_indicator)

            # chaining from card header to verify card content is displayed
            card_context = accordion_page.get_card_context(element)
            self.scroll_into_view(card_context)
            self.verify_is_displayed(card_context)

            # collapse accordion card
            element.click()
            self.scroll_into_view(element)

            # call "attribute_contains" reusable function to use custom wait with E.C. "attribute_contains"
            WebDriverWait(self.driver, 5).until(self.attribute_contains(toggle_indicator, "class", collapsed_card_indicator))

            # verify card toggle indicator is in collapsed state and card context is not displayed
            toggle_indicator_status = toggle_indicator.get_attribute("class")
            self.verify_equal(toggle_indicator_status, collapsed_card_indicator)
            self.verify_is_not_displayed(card_context)
