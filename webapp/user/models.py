from sqlalchemy import Column, Integer, String
from webapp.db.db import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(50), index=True, unique=True)
    password = Column(String(128), index=True)
    role = Column(String(20), index=True)

    def set_pasword(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f"<User {self.username}, Role: {self.role}>"