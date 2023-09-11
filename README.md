# linkedin_crawler
Crawler to get jobs from linkedin

## setting up
exec 
`$ python3 -m venv venv_linkedin_crawler`
`$ source venv_linkedin_crawler/bin/activate`
`$ pip3 install requirements.txt`

## set credentials from linkedin
`$ mv secrets-example.json secrets.json`

## run app
`$ python3 crawler/linkedin_job_scraper.py`
