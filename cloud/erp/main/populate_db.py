import os
import django
import random
from datetime import datetime, timedelta
from faker import Faker

# Django sozlamalarini o'rnatish
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp.settings")
django.setup()

from main.models import Employee


def generate_random_employees(num_employees=30):
    fake = Faker()
    positions = ["Manager", "Sales Rep", "Support", "Developer", "Analyst"]
    departments = ["Sales", "IT", "HR", "Operations", "Marketing"]

    for _ in range(num_employees):
        # Tasodifiy sana (so'nggi 5 yil ichida)
        start_date = datetime.now() - timedelta(days=5 * 365)
        hire_date = fake.date_between(start_date=start_date, end_date="today")

        # Tasodifiy ma'lumotlar
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        phone = fake.phone_number()[:20]
        position = random.choice(positions)
        department = random.choice(departments)
        salary = round(random.uniform(2000, 10000), 2)
        is_active = random.random() < 0.8  # 80% ehtimollik bilan faol

        # Xodim yaratish
        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            position=position,
            department=department,
            hire_date=hire_date,
            salary=salary,
            is_active=is_active,
        )
        print(f"Created employee: {first_name} {last_name}")


if __name__ == "__main__":
    print("Starting to add 30 random employees...")
    generate_random_employees(30)
    print("Finished adding employees.")
