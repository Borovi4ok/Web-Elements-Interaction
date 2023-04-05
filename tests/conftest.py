import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager




# "browser_name" - command line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: what browser to use to run tests"
    )


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_chrome = Service(r"C:\Disk D\Draft\QA Tester\Web Drivers\Chrome_webdriver.exe")
        driver = webdriver.Chrome(service=service_chrome)
    elif browser_name == "firefox":
        # service_firefox = Service(r"C:\Disk D\Draft\QA Tester\Web Drivers\Firefox_gecko.exe")
        # driver = webdriver.Firefox(service=service_firefox)
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        service_firefox = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_firefox)
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")
    driver.maximize_window()
    yield driver
    print(f" Cleaning up cookies and closing browser after: '{request.node.name}' is executed.")
    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture(scope="class")
def browser_setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_chrome = Service(r"C:\Disk D\Draft\QA Tester\Web Drivers\Chrome_webdriver.exe")
        driver = webdriver.Chrome(service=service_chrome)
    elif browser_name == "firefox":
        # service_firefox = Service(r"C:\Disk D\Draft\QA Tester\Web Drivers\Firefox_gecko.exe")
        # driver = webdriver.Firefox(service=service_firefox)
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        service_firefox = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_firefox)
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")
    driver.maximize_window()
    yield driver
    print(f" Cleaning up cookies and closing browser after: '{request.node.name}' is executed.")
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
            "broken": "https://demoqa.com/broken",
            "upload_download": "https://demoqa.com/upload-download",
            "dynamic_properties": "https://demoqa.com/dynamic-properties"
    }
