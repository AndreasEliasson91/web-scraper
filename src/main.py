import csv
import requests

from bs4 import BeautifulSoup
from typing import Any

BASE_URL = 'https://quotes.toscrape.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

def get_page(url: str, headers: dict) -> requests.Response:
    page = requests.get(url, headers=headers)
    return page

def web_scraping(soup: BeautifulSoup, quotes: list) -> None:
    elements = soup.find_all('div', class_='quote')

    for element in elements:
        text = element.find('span', class_='text').text
        author = element.find('small', class_='author').text
        tags = [tag.text for tag in element.select('.tags .tag')]

        quotes.append(
            {
                'text': text,
                'author': author,
                'tags': ', '.join(tags)
            }
        )

def display(counter: int, quotes: list) -> None:
    print(f' After scraping page {counter}')
    for q in quotes:
        print('Quote:', q['text'])
        print('Author:', q['author'])
        print('Tags:', q['tags'])
    print()


def main():
    quotes = list()
    page = get_page(BASE_URL, HEADERS)
    soup = BeautifulSoup(page.text, 'html.parser')
    web_scraping(soup, quotes)
    next_page_element = soup.find('li', class_='next')

    while next_page_element is not None:
        next_page_url = next_page_element.find('a', href=True)['href']
        page = get_page(BASE_URL + next_page_url, HEADERS)
        soup = BeautifulSoup(page.text, 'html.parser')
        web_scraping(soup, quotes)
        next_page_element = soup.find('li', class_='next')

    with open('quotes.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Quote', 'Quotee', 'Tags'])

        for quote in quotes:
            writer.writerow(quote.values())
    

if __name__ == '__main__':
    main()
