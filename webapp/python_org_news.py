import requests
from bs4 import BeautifulSoup
from datetime import datetime

def _get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_python_news():
    html = _get_html("https://www.python.org/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.select_one("div.medium-widget ul.menu").find_all("li")
        result_news = []
        for news in all_news:
            title = news.select_one("a").text
            date = news.select_one("time").get("datetime")
            date = datetime.strptime(date.split("T")[0], "%Y-%m-%d")
            date = datetime.strftime(date, "%d.%m.%y")
            url = news.select_one("a").get("href")
            result_news.append({
                "title": title,
                "date": date,
                "url": url
            })
        return result_news
    return False


if __name__ == "__main__":
    a = get_python_news()
    for i in a:
        print(i)

