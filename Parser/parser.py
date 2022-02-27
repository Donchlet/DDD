import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://stopgame.ru/"
URL_REVIEWS = "https://stopgame.ru/review/new/izumitelno"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    film = []

    for item in items:
        film.append(
            {
                'title': item.find('div', class_="b-content__inline_item-link").get_text(),
                'image': item.find('a', href_="").find('img').get('src')
            }
        )
    return film


@csrf_exempt
def parser_func():
    html = get_html(URL_REVIEWS)
    if html.status_code == 200:
        film = []
        for page in range(0, 1):
            html = get_html(URL_REVIEWS, params={'page': page})
            film.extend(get_data(html.text))
            return film
    else:
        raise ValueError('Error maybe permission denied')