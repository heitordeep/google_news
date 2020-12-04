from datetime import datetime
from json import dumps, loads
from os import makedirs, path

from bs4 import BeautifulSoup as bs4
from requests import get
from requests.exceptions import HTTPError

allowed_url = 'https://news.google.com/rss'


def get_news(url):
    try:
        page = get(url)
        page.raise_for_status()  # check request status.
        data = parse_news(page)
    except HTTPError as e:
        raise SystemExit(e)
    else:
        return data


def save(word, data):

    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')

    makedirs(
        path.join('raw', year, month, day), exist_ok=True
    )  # Create raw/date directory.
    path_json = path.join(
        'raw', year, month, day, f'links_{word.replace(" ", "_")}.json'
    )

    with open(path_json, 'w', encoding='utf-8') as w:
        w.write(dumps(data, ensure_ascii=False, indent=4))


def parse_news(page):
    soup = bs4(page.text, 'xml')
    payload = []
    for item in soup.find_all('item'):
        payload.append(
            {
                'title': item.find('title').text,
                'date': item.find('pubDate').text,
                'url': item.find('link').text,
            }
        )

    return payload


def main():
    with open(path.join('queries', 'config_queries.json'), 'r') as config:
        query = loads(config.read())

    for search_terms in query:
        word = search_terms['word']
        days_ago = search_terms['days_ago']
        language = search_terms['language']

        url = (
            f'{allowed_url}/search?q={word.replace(" ", "+")}+when:{days_ago}'
            f'd&hl={language}'
        )
        print(f'Procurando por {word} no google news...')
        data = get_news(url)
        save(word, data)
        print('Dados salvo com sucesso\n')


if __name__ == '__main__':
    main()
