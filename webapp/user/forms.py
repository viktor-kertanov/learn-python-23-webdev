from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control my-3"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control mb-3"})
    remember_me = BooleanField("Запомнить меня", default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField("Отправить!", render_kw={"class": "btn btn-primary"})