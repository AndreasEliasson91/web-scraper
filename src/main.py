import csv
import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://www.monster.se/'

def scrape_page(soup: BeautifulSoup, ads: list) -> None:
    pass

def get_page(url: str, ads: list) -> requests.Response:
    pass


input_values = {
    'q': 'python',
    'where': 'göteborg'
}

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page = requests.get(BASE_URL, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')
    form = soup.find('main').find('section').find('div', attrs={'aria-labelledby': 'search-hero-title'}).find('form', attrs={'data-testid': 'search-bar'})
    print(form)
    # action_url = soup.find('form', attrs={'data-testid': 'search-bar'}).get('action')
    # input_tags = soup.find_all('input')

    # for input_tag in input_tags:
    #     if input_tag.get('name') in input_values:
    #         input_tag['value'] = input_values[input_tag['q']]

    # print(action_url)

    form = soup.find(class_='sc-eCsaLi cYHLiZ')
    print(form)



if __name__ == '__main__':
    main()

