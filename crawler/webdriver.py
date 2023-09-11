from selenium import webdriver


class Driver():
    def __init__(self) -> None:
        self._driver = webdriver.Chrome()
