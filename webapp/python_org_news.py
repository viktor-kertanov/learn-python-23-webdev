import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.db.model import News
from webapp.db.db import db_session


def get_python_news():
    html = _get_html("https://www.python.org/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.select_one("div.medium-widget ul.menu").find_all("li")
        print(f"We have {len(all_news)}")
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
    news_exists = db_session.query(News).filter(News.url == url).count()
    if not news_exists:
        print(f"Title: {title}, URL: {url}, Published: {published}.")
        new_news = News(title=title, url=url, published=published)
        db_session.add(new_news)
        db_session.commit()


if __name__ == "__main__":
    a = get_python_news()

