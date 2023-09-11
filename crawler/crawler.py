import time

from selenium.webdriver.common.by import By

class Crawler():
    def __init__(self, driver, url, secrets) -> None:

        self._driver = driver
        self._url = url
        self._email = secrets["email"]
        self._password = secrets["pass"]

    def get_content_from_url(self):

        self._driver.get(self._url)
        self._driver.maximize_window()
        self._load_page()

    def do_login(self) -> bool:

        input_email = self._driver.find_element(By.ID, "username")
        input_email.click()
        input_email.send_keys(self._email)

        input_pass = self._driver.find_element(By.ID, "password")
        input_pass.click()
        input_pass.send_keys(self._password)

        login_button = (
            self._driver.find_element(By.CLASS_NAME, "login__form_action_container")
            .find_element(By.TAG_NAME, "button")
            # .find_element(By.CLASS_NAME, "from__button--floating")
        )
        login_button.click()

        self._load_page(60)

    def _load_page(self, time_sleep_default: int = 5) -> None:
        time.sleep(time_sleep_default)