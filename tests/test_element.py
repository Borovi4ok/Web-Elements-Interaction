from selenium.webdriver.common.by import By


# test suit ID_001
# text and blocks presence on 'elements' page
# key in names is 'elements'
def test_url_elements(browser, urls):
    browser.get(urls["elements"])
    assert "elements" in browser.current_url


def test_main_header_text_elements(browser):
    text = browser.find_element(By.CLASS_NAME, "main-header").text
    assert text == "Elements"


def test_main_menu_presence_elements(browser):
    assert browser.find_element(By.CLASS_NAME, "left-pannel").is_displayed()


def test_select_message_elements(browser):
    text = browser.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']").text
    assert text == "Please select an item from left to start practice."

def test_footer_text_elements(browser, cleanup):
    text = browser.find_element(By.CSS_SELECTOR, "footer span").text
    assert "ALL RIGHTS RESERVED" in text

