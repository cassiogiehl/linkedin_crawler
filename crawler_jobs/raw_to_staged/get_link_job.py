import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.config import Config
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd


class GetLinkJob:
    def __init__(self, dt_ref, source: str, sink: str) -> None:

        self.dt_ref = dt_ref
        self.html: BeautifulSoup
        self.source: str = source
        self.sink: str = sink

        self.job_links: list = []
        self.html_job_link = None

    def read_file(self) -> str:

        print(f"\nlendo arquivo html em: {self.source}{self.dt_ref}/search.html")

        with open(f"{self.source}{self.dt_ref}/search.html") as file_html:
            self.html: BeautifulSoup = BeautifulSoup(file_html, "html.parser")

    def get_job_link(self):

        print("\nbuscando links dos jobs para pagina interna")

        tag_links: BeautifulSoup = self.html.find_all("a", {"class": "base-card__full-link"})

        for a_href in tag_links:
            self.job_links.append(a_href.get("href"))

    def create_pandas_csv(self):

        print("\ntransformando link em um df com uma coluna (utl)")

        self.df = pd.DataFrame(
            self.job_links,
            columns=["desc_url_job"]
        )

        self.df.head()

    def save_html_job_links(self):

        print(f"\nsalvando os dados em {self.sink}/job_intern.csv")

        if not os.path.exists(self.sink):
            os.makedirs(self.sink)
            print("path do sink criado com sucesso!")

        else:
            print("path do sink já existe!")

        self.df.to_csv(
            f"{self.sink}/job_intern.csv",
            sep=";",
            header=True,
            index=False
        )
        print(f"arquivo csv escrito com sucesso em {self.sink}")


def get_config():

    config = Config()
    return config.read()

def get_dt_ref():

    today = date.today()
    dt_ref = today.strftime("%Y-%m-%d")

    return dt_ref

config = get_config()
dt_ref = get_dt_ref()


job = GetLinkJob(
    dt_ref,
    config["raw_to_staged"]["get_link_job"]["source"], 
    config["raw_to_staged"]["get_link_job"]["sink"] + dt_ref + "/"
    )
job.read_file()
job.get_job_link()
job.create_pandas_csv()
job.save_html_job_links()