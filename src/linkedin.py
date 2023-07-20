import csv
import time
import requests

from bs4 import BeautifulSoup

def scrapper(url, page_num):
    next_page = url + str(page_num)
    time.sleep(2)
    print(str(next_page))
    response = requests.get(str(next_page))
    print(response)
    print(page_num)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    job_title = soup.find('h3', class_='base-search-card__title').text

    print(job_title)
    if page_num < 25:
        page_num += 25
        scrapper(url, page_num)

url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=python%20developer&location=gothenburg&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start='

scrapper(url, 0)
