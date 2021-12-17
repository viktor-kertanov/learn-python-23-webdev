import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News


def get_python_news():
    html = _get_html("https://www.python.org/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.select_one("div.medium-widget ul.menu").find_all("li")
        result_news = []
        for news in all_news:
            title = news.select_one("a").text
            url = news.select_one("a").get("href")
            published = news.select_one("time").get("datetime")
            try:
                published = datetime.strptime(published.split("T")[0], "%Y-%m-%d")
            except ValueError:
                published = datetime.now()
            _save_news(title, url, published)


def _get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def _save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()


if __name__ == "__main__":
    a = get_python_news()
    for i in a:
        print(i)

