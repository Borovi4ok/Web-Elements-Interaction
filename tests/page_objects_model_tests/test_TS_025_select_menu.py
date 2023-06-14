import pytest
from WebInteractionDemoQA.page_objects.objects_TS_025_select_menu import SelectMenu
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def select_menu_page(setup):
    return SelectMenu(setup)


# Suite 25. Test Select Menu, Page Object Model
class TestSelectMenu(Assertions, ReusableFunctions):
    @pytest.mark.select_menu
    def test_url_menu(self, urls, get_excel_data):
        self.driver.get(urls["select_menu"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("025_url_select_menu", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.select_menu
    def test_select_value(self, select_menu_page):
        # expand select_value menu
        dropdown_arrow = select_menu_page.get_select_value_dropdown()
        dropdown_arrow.click()
        by_locator = select_menu_page.select_value_items
        self.explicitly_wait(by_locator, 5, "visibility_of_element_located")

        # get list of available menu items
        dropdown_items = select_menu_page.get_select_value_items()

        # define quantity of items in menu
        items_quantity = len(dropdown_items)
        message = f"There are '{items_quantity}' items in 'Select Value' menu."
        self.log_print("info", message)

        for i in range(0, items_quantity):
            # select each menu item
            dropdown_items = select_menu_page.get_select_value_items()  # to avoid 'stale element' error
            self.scroll_into_view(dropdown_items[i])
            expected_item_name = dropdown_items[i].text
            dropdown_items[i].click()

            # verify item is displayed as selected
            selected_item = select_menu_page.get_selected_value()
            actual_item_name = selected_item.text
            self.verify_equal(actual_item_name, expected_item_name)

            # loop through all menu items
            dropdown_arrow.click()
            self.explicitly_wait(by_locator, 5, "visibility_of_element_located")
        # collapse dropdown after last interaction
        dropdown_arrow.click()

    @pytest.mark.select_menu
    def test_select_one(self, select_menu_page):
        # expand select_one menu
        dropdown_arrow = select_menu_page.get_select_one_dropdown()
        self.scroll_into_view(dropdown_arrow)
        dropdown_arrow.click()
        by_locator = select_menu_page.select_one_items
        self.explicitly_wait(by_locator, 5, "visibility_of_element_located")

        # get list of available menu items
        dropdown_items = select_menu_page.get_select_one_items()

        # define quantity of items in menu
        items_quantity = len(dropdown_items)
        message = f"There are '{items_quantity}' items in 'Select One' menu."
        self.log_print("info", message)

        for i in range(0, items_quantity):
            # select each menu item
            dropdown_items = select_menu_page.get_select_one_items()  # to avoid 'stale element' error
            self.scroll_into_view(dropdown_items[i])
            expected_item_name = dropdown_items[i].text
            dropdown_items[i].click()

            # verify item is displayed as selected
            selected_item = select_menu_page.get_selected_one_value()
            actual_item_name = selected_item.text
            self.verify_equal(actual_item_name, expected_item_name)

            # loop through all menu items
            dropdown_arrow.click()
            self.explicitly_wait(by_locator, 5, "visibility_of_element_located")

        # collapse dropdown after last interaction
        dropdown_arrow.click()

    @pytest.mark.select_menu
    def test_old_style_menu(self, select_menu_page):
        # expand old style menu
        old_style_menu_dropdown = select_menu_page.get_old_style_menu_dropdown()
        self.scroll_into_view(old_style_menu_dropdown)
        old_style_menu_dropdown.click()
        by_locator = select_menu_page.old_style_menu_items
        self.explicitly_wait(by_locator, 5, "visibility_of_element_located")

        # get list of available menu items
        dropdown_items = select_menu_page.get_old_style_menu_items()
        for item in dropdown_items:
            message = f"Clicking item: '{item.text}'"
            self.log_print("info", message)
            item.click()
            self.verify_is_selected(item, is_selected=True)

    @pytest.mark.select_menu
    def test_multiselect_dropdown(self, select_menu_page):
        dropdown_arrow = select_menu_page.get_multiselect_dropdown_arrow()
        self.scroll_into_view(dropdown_arrow)
        dropdown_arrow.click()

        dropdown_items = select_menu_page.get_multiselect_dropdown_items()
        items_quantity = len(dropdown_items)
        for item in dropdown_items:
            item.click()

        dropdown_selected_items = select_menu_page.get_multiselect_dropdown_selected_items()
        selected_items_quantity = len(dropdown_selected_items)

        # verify quantity of selected items is equal to quantity of items in dropdown
        self.verify_equal(items_quantity, selected_items_quantity)

        # verify all selected items are displayed
        for item in dropdown_selected_items:
            self.verify_is_displayed(item)

    @pytest.mark.select_menu
    def test_multiselect_dropdown_delete(self, select_menu_page):
        dropdown_selected_items = select_menu_page.get_multiselect_dropdown_selected_items()
        selected_items_quantity = len(dropdown_selected_items)

        # delete first and last selected one-by-one and verify deleted
        delete_one_selected = select_menu_page.get_multiselect_dropdown_delete_one()
        delete_one_selected[0].click()
        delete_one_selected[-1].click()
        dropdown_left_items = select_menu_page.get_multiselect_dropdown_selected_items()
        left_items_quantity = len(dropdown_left_items)
        self.verify_equal(left_items_quantity, selected_items_quantity - 2)

        # delete all left at once and verify all deleted
        delete_all = select_menu_page.get_multiselect_dropdown_delete_all()
        delete_all.click()
        dropdown_shown_items = select_menu_page.get_multiselect_dropdown_selected_items()
        shown_items_quantity = len(dropdown_shown_items)
        expected_shown_items = 0
        self.verify_equal(shown_items_quantity, expected_shown_items)