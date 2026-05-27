from faker import Faker
import csv

fake = Faker('en_US')

num_rows = 600

file_name = 'random_names.csv'

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['name', 'lastname'])

    for _ in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()

        writer.writerow([first_name, last_name])

print(f'CSV file "{file_name}" created successfully!')