from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control my-3"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control mb-3"})
    submit = SubmitField("Отправить!", render_kw={"class": "btn btn-primary"})