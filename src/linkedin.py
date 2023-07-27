import requests

from bs4 import BeautifulSoup
from bs4.element import ResultSet
from datetime import date

from settings import CSV_DIR
from utils import write_to_csv

BASE_URL = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?'
URL_SUFFIX = '&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start='
KEYWORDS = ['junior', 'developer']
LOCATION = 'gothenburg'

URL = f'{BASE_URL}keywords={"%20".join(kw for kw in KEYWORDS)}&location={LOCATION}{URL_SUFFIX}'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
PARAMS = {
    'name': 'div',
    'class_': 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card'
}

def scraper(url: str, page_num: int) -> ResultSet:
    next_page = url + str(page_num)
    response = requests.get(str(next_page), timeout=10, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all(**PARAMS)
    return jobs

def linkedin_run() -> None:
    csv_file = f'../{CSV_DIR}/LINKEDIN_{date.today()}_{"-".join(kw for kw in KEYWORDS)}.csv'
    for i in range(0, 200, 25):
        jobs = scraper(URL, i)
        if jobs:
            write_to_csv(csv_file, jobs)
        else:
            break
    print('Done')
    print(URL)
