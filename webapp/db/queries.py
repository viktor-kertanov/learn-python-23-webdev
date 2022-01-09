from sqlalchemy.sql import func
from sqlalchemy import desc

from webapp.db.db import db_session
from webapp.db.model import Salary

def top_salary(num_rows):
    top_salary = db_session.query(Salary).order_by(Salary.salary.desc()).limit(num_rows)
    for s in top_salary:
        print(f"Зарплата: {s.salary}, {s.name}, {s.job}")
    return top_salary

def salary_by_city(city_name):
    top_salary = db_session.query(Salary).filter(Salary.city_name == city_name).order_by(Salary.salary.desc())
    print(city_name)
    for s in top_salary:
        print(f"Зарплата: {s.salary}, {s.name}, {s.job}")

def top_salary_by_domain(domain, num_rows):
    top_salary = db_session.query(Salary).filter(Salary.free_email.ilike(f'%{domain}')).order_by(Salary.salary.desc()).limit(num_rows)
    print(domain)
    for s in top_salary:
        print(f"Зарплата: {s.salary}, {s.name}, {s.job}, {s.free_email}")


def average_salary():
    avg_salary = db_session.query(func.avg(Salary.salary)).scalar()
    print(f"Средняя зарплата: {avg_salary:.2f}")

def count_distinct_cities():
    count_cities = db_session.query(Salary.city_name).group_by(Salary.city_name).count()
    print(f"Количество уникальных городов: {count_cities}")


def top_avg_salary_by_city(num_rows):
    top_salary = db_session.query(
        Salary.city_name,
        func.avg(Salary.salary).label('avg_salary')
    ).group_by(Salary.city_name).order_by(desc('avg_salary')).limit(num_rows)

    for city, salary in top_salary:
        print(f"City {city}, average salary: {salary:.2f}")



if __name__ == '__main__':
    top_salary(10)
    salary_by_city("Армавир")
    top_salary_by_domain("@yandex.ru", 10)
    average_salary()
    count_distinct_cities()
    top_avg_salary_by_city(10)