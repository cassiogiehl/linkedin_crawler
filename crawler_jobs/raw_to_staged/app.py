import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.config import Config
from bs4 import BeautifulSoup
from datetime import date


class RawStagedJob:
    def __init__(self, dt_ref) -> None:

        self.dt_ref = dt_ref

    def _read_file(self) -> str:

        bs4 = ""

        with open(f"data-lakedin-raw/engenheiro-machine-learning/{self.dt_ref}") as file_html:
            bs4 = BeautifulSoup(file_html, "html.parser")

        return bs4

    def get_job_link(self):

        full_link: str = self.html.find_all("a", {"class": "base-card__full-link"})
        print(full_link)


    def get_metadata(self, list_item):
        job_title: BeautifulSoup = list_item.find("h3", {"class": "base-search-card__title"})
        company_name: BeautifulSoup = (
            list_item.find("h4", {"class": "base-search-card__subtitle"})
            .find("a")
        )
        
        metadata: BeautifulSoup = list_item.find("div", {"class": "base-search-card__metadata"})
        location: BeautifulSoup = metadata.find("span", {"class": "job-search-card__location"})
        publish_Date: BeautifulSoup = metadata.find("span", {"class": "job-search-card__listdate"})

        # text_description = div.description__text .description__text--rich
        # criterios = ul.description__job-criteria-list

        pass


def get_config():

    config = Config()
    return config.read()

def get_dt_ref():

    today = date.today()
    dt_ref = today.strftime("%Y-%m-%d")

    return dt_ref

job = RawStagedJob()
