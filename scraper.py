from pprint import pprint

from bs4 import BeautifulSoup
import requests

URL = "https://habr.com/ru/all/"
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'аудиосоцсети', 'здоровье', 'Американские']


class Article:

    def __init__(self, url=URL):
        self.url = url
        self.date = str
        self.title = str
        self.link = str
        self.preview_text = str
        self.hubs = []
        self.text = str

    def get_HTML_content(self):
        html = requests.get(self.url)
        HTML_content = BeautifulSoup(html.text, features="html.parser")
        return HTML_content

    def get_articles(self, HTML_content):
        articles = HTML_content.find_all('article', class_='post post_preview')
        return articles

    def select_article_by_kw(self, articles, kw=KEYWORDS):
        tags = list(map(str.lower, KEYWORDS))

        for article in articles:

            date_el = article.find('span', class_='post__time')
            self.date = date_el.text.strip()
            title_el = article.find('a', class_='post__title_link')
            self.title = title_el.text.strip()
            self.link = title_el['href']
            self.hubs = [hub.text.strip().lower() for hub in
                         article.find_all('a', class_="inline-list__item-link hub-link")]
            preview_text_el = article.find('div', class_='post__text')
            self.preview_text = preview_text_el.text.strip().lower().split()
            article_HTML = requests.get(self.link)
            article_content = BeautifulSoup(article_HTML.text, features="html.parser")
            article_text_el = article_content.find(class_='post__text')
            self.text = article_text_el.text

            if set(tags) & set(map(str.lower, self.title.split())) or set(tags) & set(self.hubs) or set(tags) & set(
                    self.preview_text) or set(tags) & set(map(str.lower, self.text.split())):
                print(f'{self.date} - {self.title} - {self.link}')


if __name__ == '__main__':
    art_1 = Article()
    art_1.select_article_by_kw(art_1.get_articles(art_1.get_HTML_content()))










