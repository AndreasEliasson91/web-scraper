import pandas as pd
import requests

from bs4 import BeautifulSoup
from bs4.element import ResultSet

from settings import CSV_DIR, HEADERS
from utils import csv_generator, url_generator, Scraper


PARAMS = {
    'head': {
        'name': 'div',
        'class_': 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card'
    },
    'title': {
        'name': 'h3',
        'class_': 'base-search-card__title'
    },
    'company': {
        'name': 'h4',
        'class_': 'base-search-card__subtitle'
    },
    'location': {
        'name': 'span',
        'class_': 'job-search-card__location'
    },
    'link': {
        'name': 'a',
        'class_': 'base-card__full-link',
        'href': True
    },
}

def scraper(url: str, page_num: int) -> ResultSet:
    next_page = url + str(page_num)
    response = requests.get(str(next_page), timeout=10, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all(**PARAMS['head'])
    return jobs

def linkedin_run(keywords: list, location: str) -> pd.DataFrame:
    csv_file = csv_generator(Scraper.LINKEDIN, keywords, f'../{CSV_DIR}')
    url = url_generator(Scraper.LINKEDIN, keywords, location)

    data = list()
    for i in range(0, 200, 25):
        jobs = scraper(url, i)
        if jobs:
            for job in jobs:
                title = job.find(**PARAMS['title']).text.strip()
                company = job.find(**PARAMS['company']).text.strip()
                loc = job.find(**PARAMS['location']).text.strip()
                link = job.find(**PARAMS['link'])['href']
                data.append([title, company, loc, link])
        else:
            break
    
    df = pd.DataFrame(data, columns=['Title', 'Company', 'Location', 'Link'])
    # df.to_csv(csv_file)

    return df
