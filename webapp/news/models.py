from sqlalchemy import Column, Integer, String, DateTime, Text
from webapp.db.db import Base

class News(Base):
    __tablename__ = 'news'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    published = Column(DateTime, nullable=False)
    text = Column(Text, nullable=True)

    def __repr__(self):
        return f'<News {self.title} {self.url}>'