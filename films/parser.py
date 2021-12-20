import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://rezka.ag/"
URL = "https://rezka.ag/page/2/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_items')
    film = []

    for item in items:
        film.append(
            {
                'title': item.find('div', class_='b-content__inline_item-link').get_text(strip=True),
                'image': HOST + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')
            })
    print(film)
    return film

@csrf_exempt
def films_parser():
    html = get_html(URL)
    if html.status_code == 200:
        film = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            film.extend(get_content(html.text))
            return film
    else:
        raise ValueError('Error in FILMS PARSER')