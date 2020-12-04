from datetime import datetime
from json import dumps
from os import makedirs, path
from sys import argv

from bs4 import BeautifulSoup as bs4
from requests import get
from requests.exceptions import HTTPError

allowed_url = 'https://www.google.com'


def save(word, title, link):
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')

    makedirs(
        path.join('raw', year, month, day), exist_ok=True
    )  # Create raw/date directory.
    with open(
        path.join('raw', year, month, day, f'links_{word}_crawl.txt'),
        'a',
        encoding='utf-8',
    ) as f:
        f.write(f'{title} \t {link.replace("/url?q=", "")} \n')


def parse_news(word, soup, number_page):

    for content in soup.find_all(class_='ZINbbc')[1::]:

        try:
            title = content.find(class_='kCrYT').text
            link = content.find('a').get('href')
            save(word, title, link)

        except AttributeError as e:
            # TODO: Fix pagination and error handling.
            number_page += 10  # Number page.
            return number_page


def main(word, allowed_url):
    has_link = True
    number_page = 0

    while has_link:

        try:
            url = f'{allowed_url}/search?q={word}&tbm=nws&start={number_page}'
            page = get(url)
            page.raise_for_status()

            soup = bs4(page.text, 'html.parser')
            number_page = parse_news(word, soup, number_page)

            if number_page == 300:
                has_link = False
        except HTTPError as e:
            raise SystemExit(e)
            break


if __name__ == "__main__":
    params = argv[1::]
    if params:
        for word in params:
            print(f'Buscando {word} no google noticias...')
            main(word, allowed_url)
            print('Dados salvo com sucesso.')
    else:
        print('Nenhum parâmetro foi passado!')
