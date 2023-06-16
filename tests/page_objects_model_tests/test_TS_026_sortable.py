import pytest
from selenium.webdriver.common.action_chains import ActionChains
from WebInteractionDemoQA.page_objects.objects_TS_026_sortable import Sortable
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def sortable_page(setup):
    return Sortable(setup)


@pytest.fixture
def actions(setup):
    actions = ActionChains(setup)
    return actions


# Suite 26. Test Sortable, Page Object Model
class TestSortable(Assertions, ReusableFunctions):
    @pytest.mark.sortable
    def test_url_sortable(self, urls, get_excel_data):
        self.driver.get(urls["sortable"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("026_url_sortable", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.sortable
    def test_sortable_list(self, sortable_page, actions):
        # get original order of items and extract text from them
        sortable_list = sortable_page.get_list_items()
        sortable_text_list = self.extract_text_from_list(sortable_list)

        # reverse order of web elements
        for i in range(len(sortable_list)):
            actions.drag_and_drop(sortable_list[-1], sortable_list[i]).perform()

        # get order of reversed web elements and extract text from them
        sorted_list = sortable_page.get_list_items()
        sorted_text_list = self.extract_text_from_list(sorted_list)

        # reverse order of items in the original saved list
        sortable_text_list.reverse()

        # verify list of reversed web element is equal to the reversed original list
        self.verify_equal(sortable_text_list, sorted_text_list)

    @pytest.mark.sortable
    def test_sortable_grid(self, sortable_page, actions):
        # switch for grid tab
        grid_tab = sortable_page.get_grid_tab()
        grid_tab.click()

        # get original order of grid elements and extract text from them
        grid_items = sortable_page.get_grid_items()
        original_grid_items_text = self.extract_text_from_list(grid_items)

        # original quantity of elements in grid
        items_quantity = len(grid_items)

        # take any five random elements and drag them to random position
        count = 0
        while count < 5:
            source_index = self.get_random_number(items_quantity)
            target_index = self.get_random_number(items_quantity)
            actions.drag_and_drop(grid_items[source_index], grid_items[target_index]).perform()

            # make equivalent changes in the list with original order to use it as benchmark to verify actual/expected
            source_text = original_grid_items_text[source_index]
            if source_index < target_index:
                target_index += 1  # moves target element up
            original_grid_items_text.insert(target_index, source_text)  # move text respectively

            if source_index >= target_index:
                source_index += 1  # moves target element down

            original_grid_items_text.pop(source_index)  # delete duplicated text from its old position
            count += 1

        # get new actual order of elements in the grid and extract text
        sorted_grid_items = sortable_page.get_grid_items()
        sorted_grid_items_text = self.extract_text_from_list(sorted_grid_items)

        # verify actual/expected
        self.verify_equal(sorted_grid_items_text, original_grid_items_text)
        