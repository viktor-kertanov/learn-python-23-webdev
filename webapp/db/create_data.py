import csv
import random
from faker import Faker

fake = Faker('ru_RU')

def _get_fake_row():
    return [
        fake.name(),
        fake.city_name(),
        fake.street_address(),
        fake.large_company(),
        fake.job(),
        fake.phone_number(),
        fake.free_email(),
        fake.date_of_birth(minimum_age=18, maximum_age=85),
        random.randint(20000, 200000)
    ]

def generate_data(num_rows=200):
    with open('salary.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(num_rows):
            writer.writerow(_get_fake_row())


if __name__ == '__main__':
    generate_data()