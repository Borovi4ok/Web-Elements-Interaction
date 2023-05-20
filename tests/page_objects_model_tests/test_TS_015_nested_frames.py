import pytest
from WebInteractionDemoQA.page_objects.objects_TS_015_nested_frames import NestedFrames
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def nested_frames_page(setup):
    return NestedFrames(setup)


# Suite 15. Test Nested Frames, Page Object Model
class TestNestedFrames(Assertions, ReusableFunctions):
    @pytest.mark.nested_frames
    def test_url_nested_frames(self, urls, get_excel_data):
        self.driver.get(urls["nested_frames"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("015_url_nested_frames", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.nested_frames
    def test_parent_frame(self, nested_frames_page, get_excel_data):
        frame = nested_frames_page.get_parent_frame()
        self.driver.switch_to.frame(frame)
        text_element = nested_frames_page.get_parent_frame_text()
        text = text_element.text

        full_text = get_excel_data("015_parent_frame", "text_verify")
        self.verify_in_text(text, full_text)
        self.driver.switch_to.default_content()

    @pytest.mark.nested_frames
    def test_child_frame(self, nested_frames_page, get_excel_data):
        # switch to the parent frame
        parent_frame = nested_frames_page.get_parent_frame()
        self.driver.switch_to.frame(parent_frame)

        # switch to the nested (child) frame
        child_frame = nested_frames_page.get_child_frame()
        self.driver.switch_to.frame(child_frame)

        # verify text in the child iframe
        text_element = nested_frames_page.get_child_frame_text()
        text = text_element.text
        full_text = get_excel_data("015_child_frame", "text_verify")
        self.verify_in_text(text, full_text)

        self.driver.switch_to.default_content()
