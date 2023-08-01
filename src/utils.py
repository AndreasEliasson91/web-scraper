import codecs
import csv

from datetime import date
from enum import Enum


class Scraper(Enum):
    LINKEDIN = 1
    MONSTER = 2
    INDEED = 3

# TODO: Re-write this for use to other scrapers
# def write_to_csv(csv_file: str, jobs: list, page_num: int=0) -> None:
#     with codecs.open(csv_file, 'a', encoding='utf-8') as file:
#         writer = csv.writer(file, lineterminator='\n')

#         if page_num == 0:
#             writer.writerow(['Title', 'Company', 'Location', 'Link'])

#         for job in jobs:
#             title = job.find('h3', class_='base-search-card__title').text.strip()
#             company = job.find('h4', class_='base-search-card__subtitle').text.strip()
#             location = job.find('span', class_='job-search-card__location').text.strip()
#             link = job.find('a', class_='base-card__full-link', href=True)
#             writer.writerow([title, company, location, link['href']])
        
def url_generator(scraper: Scraper, keywords: list=None, location: list=None) -> str:
    url = None

    match scraper:
        case Scraper.LINKEDIN:
            url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?'
            url += f'keywords={"%20".join(kw for kw in keywords)}&'
            url += f'location={"%20".join(l for l in location)}&'
            url += 'geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start='

    return url

def csv_generator(scraper: Scraper, keywords: list=None, directory: str='/') -> str:
    return f'{directory}{scraper.name}_{date.today()}_{"-".join(kw for kw in keywords)}.csv'
