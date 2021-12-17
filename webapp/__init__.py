from flask import Flask, render_template
from webapp.model import db, News
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Новости Python"
        city = app.config["WEATHER_DEFAULT_CITY"]
        weather = weather_by_city(city)
        news = News.query.order_by(News.published.desc()).all()
        return render_template("bootstrap.html",
                               weather_html=weather,
                               current_city=city,
                               news=news,
                               webpage_title=title
                               )
    return app
