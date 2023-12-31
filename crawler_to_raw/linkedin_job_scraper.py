import os

from crawler import Crawler
from config import Config
from webdriver import Driver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import date


class LinkedinJobCrawler(Crawler):
    def __init__(
            self, 
            driver: Driver, 
            url: str, 
            sink: str
        ) -> None:
        super().__init__(driver, url)

        self.html = ""
        self.sink = sink

    def get_job_details(self):
        print("Pesquisa executada com sucesso!")

        page_html =  self.driver.page_source
        self.html = BeautifulSoup(page_html)

    def save(self):
        if self.html is "":
            self.html = "nenhum dado foi coletado!"
            print(self.html)

        if not os.path.exists(self.sink):
            os.makedirs(self.sink)
            print("path do sink criado com sucesso!")

        else:
            print("path do sink já existe!")

        sink = open(self.sink + "search.html", "w")
        sink.write(str(self.html))
        print(f"arquivo html escrito com sucesso em {self.sink}")

def get_driver():

    driver = Driver()
    return driver._driver

def get_config():

    config = Config()
    return config.read()

def get_dt_ref():

    today = date.today()
    dt_ref = today.strftime("%Y-%m-%d")

    return dt_ref

driver = get_driver()
config = get_config()
dt_ref = get_dt_ref()

search_by_job_description = LinkedinJobCrawler(
    driver = driver,
    url = config["source"],
    sink = config["sink"] + config["job_description"] + "/" + dt_ref + "/"
)
search_by_job_description.get_content_from_url()
search_by_job_description.get_job_details()
search_by_job_description.save()