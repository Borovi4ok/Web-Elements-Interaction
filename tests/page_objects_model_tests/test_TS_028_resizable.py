import pytest
from selenium.webdriver.common.action_chains import ActionChains
from WebInteractionDemoQA.page_objects.objects_TS_028_resizable import Resizable
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def resizable_page(setup):
    return Resizable(setup)


@pytest.fixture
def actions(setup):
    actions = ActionChains(setup)
    return actions


# Suite 28. Test Resizable, Page Object Model
class TestResizable(Assertions, ReusableFunctions):
    @pytest.mark.resizable
    def test_url_resizable(self, urls, get_excel_data):
        self.driver.get(urls["resizable"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("028_url_resizable", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.resizable
    def test_restricted_box_original_size(self, resizable_page, get_excel_data):
        restricted_box = resizable_page.get_restricted_box()
        initial_size = restricted_box.size
        width = initial_size['width']
        height = initial_size['height']
        size_str = f"height: {height}, width: {width}"
        expected_size = get_excel_data("028_box_original_size", "text_verify")
        self.verify_equal(size_str, expected_size)

    @pytest.mark.resizable
    def test_restricted_box_min(self, resizable_page, get_excel_data, actions):
        # define original size of the box to avoid 'MoveTargetOutOfBoundsException'
        restricted_box = resizable_page.get_restricted_box()
        initial_size = restricted_box.size
        height = initial_size['height']
        width = initial_size['width']

        # perform box resizing with Actions class
        react_resizable_handle = resizable_page.get_react_resizable_handle()
        actions.click_and_hold(react_resizable_handle).perform()
        actions.move_by_offset(-width, -height).perform()  # trying to get size '0'
        actions.release().perform()

        # retrieve new actual size of the box
        new_actual_size = restricted_box.size
        new_height = new_actual_size['height']
        new_width = new_actual_size['width']
        new_actual_size_str = f"height: {new_height}, width: {new_width}"

        # minimum allowed (restricted) box size
        min_size_allowed = get_excel_data("028_restricted_box_min", "text_verify")

        # verify actual box size is equal to minimum allowed (restricted) box size
        self.verify_equal(new_actual_size_str, min_size_allowed)

    @pytest.mark.resizable
    def test_restricted_box_max(self, resizable_page, actions):
        # define original size of the testing box and container to avoid 'MoveTargetOutOfBoundsException'
        restricted_box = resizable_page.get_restricted_box()
        box_size = restricted_box.size
        box_height = box_size['height']
        box_width = box_size['width']

        container = resizable_page.get_constraint_area()
        self.scroll_into_view(container)
        container_size = container.size
        container_height = container_size['height']
        container_width = container_size['width']

        # define max possible offset limited by 'container'
        x_offset = container_width - box_width
        y_offset = container_height - box_height

        # perform box resizing with Actions class
        react_resizable_handle = resizable_page.get_react_resizable_handle()
        actions.click_and_hold(react_resizable_handle).perform()
        actions.move_by_offset(x_offset, y_offset).perform()  # to get box size = to container size
        actions.release().perform()

        # retrieve new actual size of the box
        new_actual_size = restricted_box.size

        # verify actual box size is equal to container size
        self.verify_equal(new_actual_size, container_size)

    @pytest.mark.resizable
    def test_unrestricted_box_original_size(self, resizable_page, get_excel_data):
        unrestricted_box = resizable_page.get_unrestricted_box()
        initial_size = unrestricted_box.size
        height = initial_size['height']
        width = initial_size['width']
        size_str = f"height: {height}, width: {width}"
        expected_size = get_excel_data("028_box_original_size", "text_verify")
        self.verify_equal(size_str, expected_size)

    @pytest.mark.resizable
    def test_unrestricted_box_min(self, resizable_page, get_excel_data):
        unrestricted_box = resizable_page.get_unrestricted_box()

        # retrieve Excel data
        test_height = get_excel_data("028_unrestricted_box_min", "text_verify").split(":")[1]
        test_width = get_excel_data("028_unrestricted_box_min", "text_verify_2").split(":")[1]

        # check css restrictions on unrestricted box size
        min_css_width = unrestricted_box.value_of_css_property('min-width').strip("px")
        min_css_height = unrestricted_box.value_of_css_property('min-height').strip("px")

        # if css restrictions
        min_height = max(int(test_height), int(min_css_height))
        min_width = max(int(test_width), int(min_css_width))

        # resize box with JS Executor
        self.driver.execute_script(
            f"arguments[0].style.width = '{min_width}px'; arguments[0].style.height = '{min_height}px';",
            unrestricted_box)

        # verify resizing
        new_box_size = unrestricted_box.size
        new_height = new_box_size['height']
        new_width = new_box_size['width']
        self.verify_equal(f"{new_height}x{new_width}", f"{min_height}x{min_width}")

    @pytest.mark.resizable
    def test_unrestricted_box_max(self, resizable_page):
        # get size of the entire window and set box to the size of the window
        window_size = self.driver.get_window_size()
        max_width = window_size['width']
        max_height = window_size['height']

        unrestricted_box = resizable_page.get_unrestricted_box()
        self.driver.execute_script(
            f"arguments[0].style.width = '{max_width}px'; arguments[0].style.height = '{max_height}px';",
            unrestricted_box)

        # verify resizing
        new_box_size = unrestricted_box.size
        new_height = new_box_size['height']
        new_width = new_box_size['width']
        self.verify_equal(f"{new_height}x{new_width}", f"{max_height}x{max_width}")
