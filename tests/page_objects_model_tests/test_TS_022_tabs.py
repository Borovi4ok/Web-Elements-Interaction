import pytest
from WebInteractionDemoQA.page_objects.objects_TS_022_tabs import Tabs
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def tabs_page(setup):
    return Tabs(setup)


# Suite 22. Test Tabs, Page Object Model
class TestTabs(Assertions, ReusableFunctions):
    @pytest.mark.tabs
    def test_url_tabs(self, urls, get_excel_data):
        self.driver.get(urls["tabs"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("022_url_tabs", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.tabs
    def test_tabs(self, tabs_page):
        tabs = tabs_page.get_tabs()
        content = tabs_page.get_content()
        tabs_quantity = len(tabs)
        for i in range(0, tabs_quantity):
            tab_name = tabs[i].text
            message = f"Clicking '{tab_name}' tab."
            self.log_print("info", message)

            # to skip click if tab is disabled
            aria_disabled = tabs[i].get_attribute("aria-disabled")

            if aria_disabled is None:
                tabs[i].click()
                self.verify_is_displayed(content[i])
            elif aria_disabled == "true":
                message = f"Tab '{tab_name}' is disabled, skipping click."
                self.log_print("error", message)



