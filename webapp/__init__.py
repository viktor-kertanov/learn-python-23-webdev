from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = "Новости Python"
        city = app.config["WEATHER_DEFAULT_CITY"]
        weather = weather_by_city(city)
        news = get_python_news()
        return render_template("bootstrap.html",
                               weather_html=weather,
                               current_city=city,
                               news=news,
                               webpage_title=title
                               )
    return app
