import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import logging

from WebInteractionDemoQA.data.test_data import TestData

driver = None
default_download_dir = None

# "browser_name" - command line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: what browser to use to run tests"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    global default_download_dir
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # set the Chrome options to download files to the specified directory
        chrome_options = Options()
        default_download_dir = TestData.download_directory
        chrome_options.add_experimental_option("prefs", {"download.default_directory": default_download_dir})

        service_chrome = Service(r"C:\Disk D\Draft\QA Tester\Web Drivers\Chrome_webdriver.exe")
        driver = webdriver.Chrome(service=service_chrome, options=chrome_options)
    elif browser_name == "firefox":
        service_firefox = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_firefox)
    else:
        raise ValueError(f"\n Invalid browser name: {browser_name}")

    driver.maximize_window()
    request.cls.driver = driver
    request.cls.default_download_dir = default_download_dir
    yield driver
    print(f"\n Cleaning up cookies and closing browser after: '{request.node.name}' is executed.")
    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture
def urls():
    return {"elements": "https://demoqa.com/elements",
            "text_box": "https://demoqa.com/text-box",
            "checkbox": "https://demoqa.com/checkbox",
            "radio_button": "https://demoqa.com/radio-button",
            "webtables": "https://demoqa.com/webtables",
            "buttons": "https://demoqa.com/buttons",
            "links": "https://demoqa.com/links",
            "upload_download": "https://demoqa.com/upload-download",
            "dynamic_properties": "https://demoqa.com/dynamic-properties"
            }


@pytest.fixture
def action_chains():
    return ActionChains(driver)


"""# code - two func - that captures screenshot when TC failed and place in report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call" or report.when == "setup":
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screaenshot" style="width:304px;height;228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
                report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
"""
