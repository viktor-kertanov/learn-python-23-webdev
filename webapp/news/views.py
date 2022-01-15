from flask import Blueprint, current_app, render_template

from webapp.db.db import db_session
from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)

@blueprint.route('/')
def index():
    title = "Новости Python"
    city = current_app.config["WEATHER_DEFAULT_CITY"]
    weather = weather_by_city(city)
    news = db_session.query(News).order_by(News.published.desc()).all()
    return render_template("news/index.html",
                            weather_html=weather,
                            current_city=city,
                            news=news,
                            webpage_title=title
                            )