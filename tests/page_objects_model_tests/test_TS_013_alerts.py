import pytest
from WebInteractionDemoQA.page_objects.objects_TS_013_alerts import Alerts
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from WebInteractionDemoQA.data.excel_data import get_excel_data


@pytest.fixture
def alerts_page(setup):
    return Alerts(setup)


# Suite 13. Test Alerts, Page Object Model
class TestAlerts(Assertions, ReusableFunctions):
    @pytest.mark.alerts
    def test_url_alerts(self, urls, get_excel_data):
        self.driver.get(urls["alerts"])

        # get_excel_data(TS#_TC_name, key)
        expected_url = get_excel_data("013_url_alerts", "text_verify")
        self.verify_url(expected_url)

    @pytest.mark.alerts
    def test_alert(self, alerts_page, get_excel_data):
        alerts_page.get_alert_button().click()

        # call "wait" reusable function
        ec_condition = "alert_is_present"
        self.explicitly_wait(False, 7, ec_condition)

        # get text from alert and verify it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        expected_text = get_excel_data("013_alert", "text_verify")
        self.verify_in_text(alert_text, expected_text)
        alert.accept()

    @pytest.mark.alerts
    def test_delayed_alert(self, alerts_page, get_excel_data):
        alerts_page.get_delayed_alert_button().click()

        # call "wait" reusable function
        ec_condition = "alert_is_present"
        self.explicitly_wait(False, 7, ec_condition)

        # switch to the alert and verify text
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        expected_text = get_excel_data("013_delayed_alert", "text_verify")
        self.verify_in_text(alert_text, expected_text)
        alert.accept()

    @pytest.mark.alerts
    def test_confirm_accept(self, alerts_page, get_excel_data):
        # click "confirm box" button
        alerts_page.get_confirm_button().click()

        # call "wait" reusable function
        ec_condition = "alert_is_present"
        self.explicitly_wait(False, 5, ec_condition)

        # extract text from "confirm box" and verify it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        expected_text = get_excel_data("013_confirm_accept", "text_verify")
        self.verify_in_text(alert_text, expected_text)

        # accept "confirm" and verify success message
        alert.accept()
        result_element = alerts_page.get_confirm_result_message()
        result_message = result_element.text
        expected_text = get_excel_data("013_confirm_accept", "text_verify_2")
        self.verify_in_text(result_message, expected_text)

    @pytest.mark.alerts
    def test_confirm_dismiss(self, alerts_page, get_excel_data):
        # click "confirm box" button
        alerts_page.get_confirm_button().click()

        # call "wait" reusable function
        ec_condition = "alert_is_present"
        self.explicitly_wait(False, 5, ec_condition)

        # extract text from "confirm box" and verify it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        expected_text = get_excel_data("013_confirm_dismiss", "text_verify")
        self.verify_in_text(alert_text, expected_text)

        # dismiss "confirm" and verify decline message
        alert.dismiss()
        result_element = alerts_page.get_confirm_result_message()
        result_message = result_element.text
        expected_text = get_excel_data("013_confirm_dismiss", "text_verify_2")
        self.verify_in_text(result_message, expected_text)

    @pytest.mark.alerts
    def test_prompt(self, alerts_page, get_excel_data):
        # click "prompt" button
        alerts_page.get_prompt_button().click()

        # call "wait" reusable function
        ec_condition = "alert_is_present"
        self.explicitly_wait(False, 5, ec_condition)

        # extract text from "prompt" and verify it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        expected_text = get_excel_data("013_prompt", "text_verify")
        self.verify_in_text(alert_text, expected_text)

        # enter name in prompt
        name = get_excel_data("013_prompt", "name")
        alert.send_keys(name)
        alert.accept()

        # verify name in success message
        result_element = alerts_page.get_prompt_result_message()
        result_message = result_element.text
        self.verify_in_text(name, result_message)
