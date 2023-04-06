import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def assert_in_url(self, text):
        assert text in self.driver.current_url
        print(f"{text} is asserted.")
