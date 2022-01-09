from sqlalchemy import Column, Integer, String, Date, DateTime, Text
from webapp.db.db import Base, engine


class Salary(Base):
    __tablename__ = 'salaries'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_name = Column(String)
    street_address = Column(String)
    large_company = Column(String)
    job = Column(String)
    phone_number = Column(String)
    free_email = Column(String)
    date_of_birth = Column(Date)
    salary = Column(Integer)

    def __repr__(self):
        return f"Salary {self.id}, {self.name}, {self.company}"


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


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)