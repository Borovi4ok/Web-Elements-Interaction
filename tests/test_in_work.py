from selenium.webdriver.common.by import By
from WebInteractionDemoQA.test_data.data_test_elements import DataElements


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
    browser.find_element(By.ID, "submit").click()


def test_output_text_box(browser, cleanup):
    data = DataElements.data_text_box

    elements_list = browser.find_elements(By.CLASS_NAME, "mb-1")

    output_list = [element.text for element in elements_list]

    for i in range(0, 4):
        assert data[i] in output_list[i]