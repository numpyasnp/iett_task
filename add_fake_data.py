import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vehicle_tracking.settings")

import django

django.setup()
from faker import Faker
from driver.models import Driver
from user.models import User


def add_driver():
    fake = Faker(["en_US"])
    drivers = []
    for i in range(10000):
        user = create_user()
        while True:
            license_number = fake.random_number(digits=20, fix_len=True)
            driver = Driver.objects.filter(license_number=license_number)
            if not driver.exists():
                break
        try:
            driver = Driver(license_number=license_number, user=user)
            drivers.append(driver)
            print("add driver -> ", i)
        except Exception as e:
            print("set_driver err", e)

    Driver.objects.bulk_create(drivers)


def create_user():
    fake = Faker(["en_US"])
    name = fake.first_name()
    while True:
        personal_id = fake.random_number(digits=11, fix_len=True)
        user = User.objects.filter(personal_id=personal_id)
        if not user.exists():
            break
    user = User.objects.create(personal_id=personal_id, name=name)
    user.save(update_fields=("password",))
    print("user: ", user)
    return user


add_driver()
