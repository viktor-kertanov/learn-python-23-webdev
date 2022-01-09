import csv
import time

from webapp.db.db import db_session
from webapp.db.model import Salary


def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = [
            'name',
            'city_name',
            'street_address',
            'large_company',
            'job',
            'phone_number',
            'free_email',
            'date_of_birth',
            'salary'
        ]
        reader = csv.DictReader(f, fields, delimiter=';')
        salary_data = [row for row in reader]
        _save_salary_data(salary_data)

def _save_salary_data(data):
    db_session.bulk_insert_mappings(Salary, data)
    db_session.commit()

if __name__ == "__main__":
    start = time.time()
    read_csv("webapp/db/salary.csv")
    print(f"Загрузка заняла: {time.time() -  start} секунд.")