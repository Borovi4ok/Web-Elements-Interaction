from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements

# text and blocks presence on "elements" page
# key to run is "elements"

from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements
from WebInteractionDemoQA.utilities import use_fixtures


# text and blocks presence on "elements" page
# key to run is "elements"
def test_url_elements(browser, urls):
    browser.get(urls["elements"])
    use_fixtures.assert_in_url(browser, "element")
