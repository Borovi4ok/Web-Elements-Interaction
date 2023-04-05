from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements


# text and blocks presence on "elements" page
# key in names is "elements"
def test_url_elements(browser, urls):
    browser.get(urls["elements"])
    assert "elements" in browser.current_url


def test_main_header_text_elements(browser):
    text = browser.find_element(By.CLASS_NAME, "main-header").text
    assert text == "Elements"


def test_main_menu_presence_elements(browser):
    box = browser.find_element(By.CLASS_NAME, "left-pannel")
    assert box.is_displayed()


def test_select_message_elements(browser):
    text = browser.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']").text
    assert text == "Please select an item from left to start practice."


def test_footer_text_elements(browser):
    text = browser.find_element(By.CSS_SELECTOR, "footer span").text
    assert "ALL RIGHTS RESERVED" in text


# text-box, submit form on "text_box" page
# key in names is "text_box"
def test_url_text_box(browser, urls):
    browser.get(urls["text_box"])
    assert "text-box" in browser.current_url


def test_text_box(browser):
    data = DataElements.data_text_box

    # full name field
    browser.find_element(By.CSS_SELECTOR, "input#userName").send_keys(data[0])

    # email field
    browser.find_element(By.XPATH, "//input[@type='email']").send_keys(data[1])

    # current address field
    browser.find_element(By.CSS_SELECTOR, "textarea#currentAddress").send_keys(data[2])

    # permanent address field
    browser.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys(data[3])

    # submit button
    element = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].scrollIntoView();", element)
    element.click()


def test_output_text_box(browser):
    data = DataElements.data_text_box
    elements_list = browser.find_elements(By.CLASS_NAME, "mb-1")
    output_list = [element.text for element in elements_list]
    for i in range(0, 4):
        assert data[i] in output_list[i]