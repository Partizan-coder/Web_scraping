import requests
from bs4 import BeautifulSoup

response = requests.get('https://habr.com/ru/all/')
KEYWORDS = {'дизайн', 'фото', 'Программирование', 'python', 'Сетевое оборудование'}


if not response.ok:
    raise ValueError('No response')

text = response.text
soup = BeautifulSoup(text, features="html.parser")
articles = soup.find_all('article')

for article in articles:
    hubs = {h.text for h in article.find_all('a', class_='tm-article-snippet__hubs-item-link')}
    if KEYWORDS & hubs:
        time_post = article.find(class_="tm-article-snippet__datetime-published").time.get('title')[:10]
        header = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").text
        href = article.find('a', class_="tm-article-snippet__title-link").attrs.get('href')
        print(f"{time_post}    \"{header}\"    https://habr.com{href}")
