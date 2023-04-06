import pytest


@pytest.mark.usefixtures("setup")
class Assertions:
    def verify_url(self, text):
        try:
            assert text in self.driver.current_url
        except AssertionError:
            print(f"\n Assertion failed: {text} not found in URL")
            raise
        else:
            print(f"\n {text} is asserted.")

    @staticmethod
    def verify_text_equal(text_actual, text_expect):
        try:
            assert text_actual == text_expect
        except AssertionError:
            print(f"\n Assertion failed: actual text '{text_actual}' is not equal to expected '{text_expect}'")
            raise
        else:
            print(f"\n {text_actual} is asserted.")

    @staticmethod
    def verify_in_text(short_text, full_text):
        try:
            assert short_text in full_text
        except AssertionError:
            print(f"\n Assertion failed: text '{short_text}' is not present in full text '{full_text}'")
            raise
        else:
            print(f"\n {short_text} is asserted.")

    @staticmethod
    def verify_is_displayed(element):
        try:
            assert element.is_displayed()
        except AssertionError:
            print(f"\n Assertion failed: element not found")
            raise
        else:
            print(f"\n Element is asserted.")
