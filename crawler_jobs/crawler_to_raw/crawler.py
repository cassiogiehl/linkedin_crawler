import time

from webdriver import Driver

class Crawler():
    def __init__(self, driver: Driver, url: str) -> None:

        self.driver = driver
        self.url = url

    def get_content_from_url(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self._load_page()

    def _load_page(self, time_sleep_default: int = 5) -> None:
        time.sleep(time_sleep_default)