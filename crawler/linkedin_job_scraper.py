from crawler import Crawler
from config import Config, Secrets
from webdriver import Driver


class LinkedinJobCrawler(Crawler):
    def __init__(self, driver, url, secrets) -> None:
        super().__init__(driver, url, secrets)

        # scrap
        self.get_content_from_url()
        self.do_login()


    # def _do_search(self, job_title: str):

    #     input_search = (
    #         self.chrome_driver.find_element(By.TAG_NAME, "input")
    #             .find_element(By.ID, "jobs-search-box-keyword-id-ember24")
    #     )

    #     print("\nInput search")

    #     input_search.send_keys(job_title)

    #     print("\nSend Keys")

    #     side_bar = self.chrome_driver.find_element(By.CLASS_NAME, "scaffold-layout__list")
    #     result_list = side_bar.find_element(By.CLASS_NAME, "jobs-search-results-list")
    #     jobs_list = result_list.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
    #     jobs = jobs_list.find_elements(By.TAG_NAME, "li")

    #     return jobs




def get_driver():

    driver = Driver()
    return driver._driver

def get_url_search() -> str:

    config = Config()
    file = config.read()
    url_search = file["url_search"]
    return url_search

def get_secrets():

    secrets = Secrets()
    return secrets.read()


driver = get_driver()
url_search = get_url_search()
secrets = get_secrets()


LinkedinJobCrawler(
    driver,
    url_search,
    secrets
)