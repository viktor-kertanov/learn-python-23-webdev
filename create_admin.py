from getpass import getpass
import sys

from webapp import create_app
from webapp.user.models import User
from webapp.db.db import db_session

app = create_app()

with app.app_context():
    username = input('Введитее имя: ')

    if db_session.query(User).filter(User.username == username).count():
        print("Пользователь с таким именем уже существует.")
        sys.exit(0)
    
    password1 = getpass("Введите пароль: ")
    password2 = getpass("Повторите пароль: ")

    if not password1 == password2:
        print("Пароли не одинаковые.")
        sys.exit(0)
    
    new_user = User(username=username, role="admin")
    new_user.set_pasword(password1)

    db_session.add(new_user)
    db_session.commit()
    print(f"Создан пользователь с id={new_user.id}, username={new_user.username}")