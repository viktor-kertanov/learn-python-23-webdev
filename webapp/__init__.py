from flask import Flask, render_template
from webapp.db.db import db_session
from webapp.db.model import News
from webapp.weather import weather_by_city
from webapp.db.queries import top_salary
from webapp.forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = "Новости Python"
        city = app.config["WEATHER_DEFAULT_CITY"]
        weather = weather_by_city(city)
        news = db_session.query(News).order_by(News.published.desc()).all()
        return render_template("bootstrap.html",
                               weather_html=weather,
                               current_city=city,
                               news=news,
                               webpage_title=title
                               )
    
    @app.route('/pagination')
    def pagination():
        title = "Testing pagination"
        salaries = top_salary(200)
        return render_template("pagination.html",
                               webpage_title=title,
                               salaries=salaries)
    
    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template("login.html", page_title=title, form=login_form)
    
    return app
