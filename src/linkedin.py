import codecs
import csv
import time
import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=python%20developer&location=gothenburg&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start='
DATE = '2023-07-25'
PAGE = 'LINKEDIN'
KEYWORDS = ['python', 'developer']

def linkedin_scraper(url: str, page_num: int) -> None:
    next_page = url + str(page_num)
    # time.sleep(2)
    print(str(next_page))
    response = requests.get(str(next_page), timeout=10)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup.prettify())
    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    csv_file = f'{PAGE}_{DATE}_{"-".join(kw for kw in KEYWORDS)}.csv    '

    with codecs.open(csv_file, 'w+', encoding='utf-8') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(['Title', 'Company', 'Location', 'Apply'])

        for job in jobs:
            writer.writerow([
                job.find('h3', class_='base-search-card__title').text.strip(),
                job.find('h4', class_='base-search-card__subtitle').text.strip(),
                job.find('span', class_='job-search-card__location').text.strip().encode('utf-8'),
                job.find('a', class_='base-card__full-link').text.strip(),
            ])

        # print(f'Title: {title} : Company: {company} : Location: {location}\nURL: {link}')

    if page_num < 25:
        page_num += 25
        linkedin_scraper(url, page_num)


linkedin_scraper(BASE_URL, 0)
