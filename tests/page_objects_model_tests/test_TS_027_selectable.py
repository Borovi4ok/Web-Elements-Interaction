import pytest
from WebInteractionDemoQA.page_objects.objects_TS_027_selectable import Selectable
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def selectable_page(setup):
    return Selectable(setup)


# Suite 27. Test Selectable, Page Object Model
class TestSelectable(Assertions, ReusableFunctions):
    @pytest.mark.selectable
    def test_url_selectable(self, urls, get_excel_data):
        self.driver.get(urls["selectable"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("027_url_selectable", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.selectable
    def test_selectable_list(self, selectable_page, get_excel_data):
        list_items = selectable_page.get_list_items()

        # 'selected' indicator in the class name of selected element
        selection_indicator = get_excel_data("027_selectable", "text_verify")

        for item in list_items:
            item.click()
            # verify 'selected' indicator is present in class name of element - selected
            class_value = item.get_attribute("class")
            self.verify_in_text(selection_indicator, class_value)

            item.click()
            # verify 'selected' indicator is not present in class name of element - unselected
            class_value = item.get_attribute("class")
            self.verify_not_in_text(selection_indicator, class_value)

    @pytest.mark.selectable
    def test_selectable_grid(self, selectable_page, get_excel_data):
        grid_tab = selectable_page.get_grid_tab()
        grid_tab.click()

        grid_items = selectable_page.get_grid_items()

        # 'selected' indicator in the class name of selected element
        selection_indicator = get_excel_data("027_selectable", "text_verify")

        for item in grid_items:
            item.click()
            # verify 'selected' indicator is present in class name of element - selected
            class_value = item.get_attribute("class")
            self.verify_in_text(selection_indicator, class_value)

            item.click()
            # verify 'selected' indicator is not present in class name of element - unselected
            class_value = item.get_attribute("class")
            self.verify_not_in_text(selection_indicator, class_value)

