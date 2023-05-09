import os
import pytest
from WebInteractionDemoQA.data.test_data import TestData
from WebInteractionDemoQA.utilities.assert_functions import Assertions
from WebInteractionDemoQA.utilities.reusable_functions import ReusableFunctions
from selenium.webdriver.common.by import By


# Suite 9. Test File Transfer, Classic Model
class TestFileTransfer(Assertions, ReusableFunctions):
    @pytest.mark.file_transfer
    def test_url_file_transfer(self, urls):
        self.driver.get(urls["upload_download"])
        self.verify_url("upload-download")

    @pytest.mark.file_transfer
    def test_download(self):
        self.driver.find_element(By.ID, "downloadButton").click()
        download_file_path = os.path.join(self.default_download_dir, TestData.file_name)

        # call assertion, wait for download and verify path to the file was created
        self.verify_path_exists(download_file_path, 60)

    @pytest.mark.file_transfer
    def test_upload(self):
        # send keys with file path directly to <input>, without click
        # "default_download_dir" is defined in conftest.py "setup"
        file_input = self.driver.find_element(By.CSS_SELECTOR, "input#uploadFile")
        upload_file_path = (self.default_download_dir + TestData.file_name)

        file_input.send_keys(upload_file_path)
        success_message = self.driver.find_element(By.ID, "uploadedFilePath")
        self.verify_is_displayed(success_message)
        self.verify_in_text(TestData.file_name, success_message.text)
