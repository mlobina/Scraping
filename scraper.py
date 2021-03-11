from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://habr.com/ru/all/"
KEYWORDS = ['дизайн', 'фото', 'web', 'python']


class Article:

    def __init__(self, url=URL):
        self.url = url
        self.date = str
        self.title = str
        self.link = str


    def get_HTML_content(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception('bad response')
        HTML_content = response.text
        return HTML_content

    def get_articles(self, HTML_content):
        bsObj = BeautifulSoup(HTML_content, features='html.parser')
        articles = bsObj.find_all('article', class_='post post_preview')
        return articles

    def select_article_by_kw_in_hubs(self, articles):
        for article in articles:
            articles_hubs = [hub.text.strip().lower() for hub in article.find_all('a', class_="inline-list__item-link hub-link")]
            for hub in articles_hubs:
                if any(kw in hub for kw in KEYWORDS):
                    title_el = article.find('a', class_="post__title_link")
                    self.title = title_el.text.strip()
                    self.link = title_el['href']
                    date_el = article.find('span', class_="post__time")
                    self.date = date_el.text.strip()
                    print(f'<{self.date}> - <{self.title}> - <{self.link}> ({hub})')



    def main(self):
        print(self.select_article_by_kw_in_hubs(self.get_articles(self.get_HTML_content())))

if __name__ == '__main__':
    art_1 = Article()
    art_1.select_article_by_kw_in_hubs(art_1.get_articles(art_1.get_HTML_content()))










