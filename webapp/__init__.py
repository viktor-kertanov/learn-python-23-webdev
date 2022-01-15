from flask import Flask
from flask_login import LoginManager

from webapp.db.db import db_session
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.news.views import blueprint as news_blueprint
from webapp.salary.views import blueprint as salary_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login"
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(salary_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return db_session.query(User).get(user_id)
        
    return app
