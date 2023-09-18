import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import requests
import pandas as pd
import json
from utils.config import Config
from bs4 import BeautifulSoup
from datetime import date


class StagedCuratedJob:
    def __init__(self, dt_ref, source: str, sink: str) -> None:

        self.dt_ref = dt_ref
        self.html: BeautifulSoup
        self.source: str = source
        self.sink: str = sink
        self.df_new: pd.DataFrame

    def read_df(self) -> str:

        print("\nlendo pandas df")

        self.df = pd.read_csv(f"{self.source}")

    def get_details_from_job_intern_page(self):

        print("\nget_details")

        json_job_details = {}
        self.df_new = self.df

        for url_job_intern in self.df["desc_url_job"].to_list():
            req = requests.get(
                url_job_intern
            )
            html = req.content
            html_bs4 = BeautifulSoup(html, "html.parser")
            job_details = html_bs4.find("script", {"type": "application/ld+json"}).get_text()
            json_job_details = json.loads(job_details)
            df_job = pd.DataFrame.from_dict(json_job_details)
            df_job["desc_url_job"] = url_job_intern

            self.df_new = pd.concat([self.df_new, df_job])

    def save_html_job_links(self):
        if not os.path.exists(self.sink):
            os.makedirs(self.sink)
            print("path do sink criado com sucesso!")

        else:
            print("path do sink já existe!")

        self.df_new.to_csv(
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


job = StagedCuratedJob(
    dt_ref,
    config["staged_to_curated"]["get_job_details"]["source"] + dt_ref + "/job_intern.csv", 
    config["staged_to_curated"]["get_job_details"]["sink"] + dt_ref + "/"
    )
job.read_df()
job.get_details_from_job_intern_page()
job.save_html_job_links()