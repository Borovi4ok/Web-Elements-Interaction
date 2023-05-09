import pytest
from selenium.webdriver.common.by import By
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
import inspect


# Suite 4. Test radio-buttons, Classic Model
class TestRadioButtons(Assertions, ReusableFunctions):

    @pytest.mark.radio
    def test_url_radio_button(self, urls):
        self.driver.get(urls["radio_button"])
        self.verify_url("radio-button")

    @pytest.mark.radio
    def test_select_radio_buttons(self):
        test_func_name = inspect.stack()[1][3]
        log = Assertions.get_logger()

        radio_buttons_click_list = self.driver.find_elements(By.CLASS_NAME, "custom-control-label")
        # list of radio buttons with clickable locators

        radio_buttons_selected_list = self.driver.find_elements(By.CSS_SELECTOR, "input[type='radio'][name='like']")
        # list of radio buttons with input[type='radio'] locators applicable for .is_selected method

        clickable_radios_count = len(radio_buttons_click_list)
        selected_radios_count = len(radio_buttons_selected_list)
        self.verify_equal(clickable_radios_count, selected_radios_count)
        # verify both lists found equal number of radio buttons

        for i in range(0, clickable_radios_count):
            if not radio_buttons_selected_list[i].is_enabled():
                log.info(f"\n Test function '{test_func_name }': Radio button with index {i} is disable, skipping click.")
                continue

            radio_buttons_click_list[i].click()

            self.verify_is_selected(radio_buttons_selected_list[i], is_selected=True)
            # verify if selected

            if i > 0:
                self.verify_is_selected(radio_buttons_selected_list[i - 1], is_selected=False)
                # verify if previous unselected (=False)

            elif i == clickable_radios_count - 1:
                radio_buttons_click_list[0].click()
                self.verify_is_selected(radio_buttons_selected_list[i], is_selected=False)
                # click first radio button and verify if last one unselected (=False)
