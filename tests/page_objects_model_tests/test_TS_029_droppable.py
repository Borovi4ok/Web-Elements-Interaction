import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from WebInteractionDemoQA.page_objects.objects_TS_029_droppable import Droppable
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def droppable_page(setup):
    return Droppable(setup)


@pytest.fixture
def actions(setup):
    actions = ActionChains(setup)
    return actions


# Suite 29. Test Droppable, Page Object Model
class TestDroppable(Assertions, ReusableFunctions):
    @pytest.mark.droppable
    def test_url_droppable(self, urls, get_excel_data):
        self.driver.get(urls["droppable"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("029_url_droppable", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.droppable
    def test_simple_droppable(self, droppable_page, actions):
        source_box = droppable_page.get_simple_draggable()
        target_box = droppable_page.get_simple_droppable()

        by_locator = droppable_page.simple_droppable
        initial_text = target_box.text

        actions.drag_and_drop(source_box, target_box).perform()

        # custom wait for text to change = assertion
        self.wait_for_text_change(by_locator, initial_text)

    @pytest.mark.droppable
    def test_accept_droppable(self, droppable_page, actions):
        accept_tab = droppable_page.get_accept_tab()
        accept_tab.click()

        target_box = droppable_page.get_accept_droppable()
        target_box_location = target_box.location
        target_box_x = target_box_location['x']
        target_box_y = target_box_location['y']

        source_boxes = droppable_page.get_accept_draggable()

        # use in custom wait for text to change in target_box
        by_locator = droppable_page.accept_droppable

        for box in reversed(source_boxes):
            # first the last (not acceptable) - text should not be changed
            target_box_text = target_box.text

            source_box_location = box.location
            source_box_x = source_box_location['x']
            source_box_y = source_box_location['y']
            offset_x = target_box_x - source_box_x
            offset_y = target_box_y - source_box_y
            actions.click_and_hold(box).move_by_offset(offset_x, offset_y).release().perform()
            self.wait_for_text_change(by_locator, target_box_text)

    @pytest.mark.droppable
    def test_prevent_propagation_not_greedy(self, droppable_page, actions):
        # logic - both not_greedy outer and inner boxes should change text when source box dropped into inner box

        # get prevent propagation tab
        prevent_propagation_tab = droppable_page.get_prevent_propagation_tab()
        prevent_propagation_tab.click()

        # get source box (draggable) location
        source_box = droppable_page.get_prevent_propagation_draggable()

        # get target box (droppable)
        target_outer_box = droppable_page.get_not_greedy_outer_droppable()
        target_inner_box = droppable_page.get_not_greedy_inner_droppable()

        # get target boxes text for verification
        target_outer_box_text = target_outer_box.text
        target_inner_box_text = target_inner_box.text

        # perform drag_and_drop action
        actions.drag_and_drop(source_box, target_inner_box).perform()

        # wait for text to change in inner target box
        by_locator = droppable_page.not_greedy_inner_droppable
        self.wait_for_text_change(by_locator, target_inner_box_text)

        # get updated text in outer and inner boxes
        new_target_outer_box_text = target_outer_box.text
        new_target_inner_box_text = target_inner_box.text

        # verify text has changed in both not_greedy boxes synchronously
        self.verify_in_text(new_target_inner_box_text, new_target_outer_box_text)

        # verify initial text in outer target box has changed
        self.verify_not_in_text(target_outer_box_text, new_target_outer_box_text)

    @pytest.mark.droppable
    def test_prevent_propagation_greedy(self, droppable_page, actions):
        # logic - both greedy outer and inner boxes react separately on drop

        def drag_drop_verify(by_locator, target_box, target_box_text):
            # get source box (draggable) location
            source_box = droppable_page.get_prevent_propagation_draggable()
            source_box_location = source_box.location
            source_box_x = source_box_location["x"]
            source_box_y = source_box_location["y"]

            target_box_location = target_box.location
            target_box_x = target_box_location["x"]
            target_box_y = target_box_location["y"]

            # calculate offset to drag source_box to the inner greedy box
            offset_x = target_box_x - source_box_x
            offset_y = target_box_y - source_box_y

            self.scroll_into_view(source_box)

            # drag and drop source box to inner box (should change text in inner box only)
            actions.drag_and_drop_by_offset(source_box, offset_x, offset_y).perform()

            # wait and verify text to be changed
            self.wait_for_text_change(by_locator, target_box_text)

        # extract text from outer box for verification
        outer_box = droppable_page.get_greedy_outer_droppable()
        # chaining to the <p> element to extract text from outer box (parent) only
        outer_box_text = droppable_page.get_greedy_outer_droppable_text(outer_box).text

        # drag and drop to inner box, outer should not change
        inner_box = droppable_page.get_greedy_inner_droppable()
        inner_box_text = inner_box.text
        by_locator = droppable_page.greedy_inner_droppable
        drag_drop_verify(by_locator, inner_box, inner_box_text)

        # verify outer box text was not changed
        refresh_outer_box = droppable_page.get_greedy_outer_droppable()
        # chaining to the <p> element to extract text from outer box (parent) only
        refresh_outer_box_text = droppable_page.get_greedy_outer_droppable_text(outer_box).text
        self.verify_equal(refresh_outer_box_text, outer_box_text)

        # drag and drop to outer box
        by_locator = droppable_page.greedy_outer_droppable
        drag_drop_verify(by_locator, refresh_outer_box, refresh_outer_box_text)

    @pytest.mark.droppable
    def test_revertable(self, droppable_page, actions):
        # logic - when drop draggable in droppable revertable_box should change text and revert to its original position

        revert_droppable_tab = droppable_page.get_revert_droppable_tab()
        revert_droppable_tab.click()

        target_box = droppable_page.get_revert_droppable_box()
        target_box_text = target_box.text

        revertable_box = droppable_page.get_revertable_box()
        revertable_box_location = revertable_box.location

        # drag, drop and wait for text in droppable box to change
        by_locator = droppable_page.revert_droppable_box
        actions.drag_and_drop(revertable_box, target_box).perform()
        self.wait_for_text_change(by_locator, target_box_text)

        # wait for reventable box to take its original place
        time.sleep(0.5)

        new_revertable_box_location = revertable_box.location
        self.verify_equal(new_revertable_box_location, revertable_box_location)

    @pytest.mark.droppable
    def test_not_revertable(self, droppable_page, actions):
        # logic - when drop draggable in droppable not_revertable_box should change text and remain in droppable

        # refresh page to get back original text in droppable box
        self.driver.refresh()
        by_locator = droppable_page.revert_droppable_tab
        self.explicitly_wait(by_locator, 5, "visibility_of_element_located")

        # switch the tab for revert_droppable_tab
        revert_droppable_tab = droppable_page.get_revert_droppable_tab()
        revert_droppable_tab.click()

        target_box = droppable_page.get_revert_droppable_box()
        target_box_text = target_box.text

        not_revertable_box = droppable_page.get_revertable_box()

        # drag, drop and wait for text in droppable box to change
        by_locator = droppable_page.revert_droppable_box
        actions.drag_and_drop(not_revertable_box, target_box).perform()
        self.wait_for_text_change(by_locator, target_box_text)