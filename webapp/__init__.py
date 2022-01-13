from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from webapp.db.db import db_session
from webapp.db.model import News, User
from webapp.weather import weather_by_city
from webapp.db.queries import top_salary
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        return db_session.query(User).get(user_id)

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
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template("login.html", page_title=title, form=login_form)
    
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = db_session.query(User).filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash("Вы успешно вошли на сайт!")
                return redirect(url_for('index'))
        flash("Неправильное имя или пароль")
        return redirect(url_for('login'))
    
    @app.route('/logout')
    def logout():
        logout_user()
        flash("Вы успешно разлогинились.")
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return "Привет админ!"
        else:
            return "Ты не админ!"
        
    return app
