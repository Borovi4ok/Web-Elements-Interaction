

def assert_in_url(browser, text):
    assert text in browser.current_url
    print(f"{text} is asserted.")
