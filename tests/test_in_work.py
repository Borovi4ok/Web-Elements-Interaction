from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = "\Disk D\Draft\QA Tester\Chrome_webdriver\chromedriver"
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver.get("https://demoqa.com/elements")
driver.get("https://rahulshettyacademy.com")
driver.implicitly_wait(5)  # wait for 5 sec if element is not found


"""import random
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from WebInteractionDemoQA.data.test_data import TestData
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.webdriver.common.by import By


# Suite 5. Test Web Tables
class TestElementsPage(Assertions, ReusableFunctions):

    @pytest.mark.webtables
    def test_url_webtable(self, urls):
        self.driver.get(urls["webtables"])
        self.verify_url("webtables")

    @pytest.mark.webtables
    def test_webtable_edit_row(self):
        # click edit button and edit a value from each column

        rows_list = self.get_column_data(1, 0)
        rows_amount = len(rows_list)
        # take a list of filled rows in first column and define a number of filled rows

        print(f"rows_amount = {rows_amount}")

        test_row_ind = random.randrange(1, rows_amount)
        # index of a row to test in this test run
        print(f" test_row_ind = {test_row_ind}")

        self.driver.find_element(By.ID, f"edit-record-{test_row_ind}")

        registration_form_fields = self.driver.find_elements(By.CSS_SELECTOR, ".mr-sm-2.form-control")

        for i in range(0, len(registration_form_fields)):
            registration_form_fields[i].clean()
            registration_form_fields[i].send_keys(TestData.data_edit_table[i])

        self.driver.find_element(By.ID, "submit").click()
"""