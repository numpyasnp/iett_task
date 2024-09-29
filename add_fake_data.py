import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vehicle_tracking.settings")
import django

django.setup()

import random
from faker import Faker
from driver.models import Driver
from location.models import Location
from vehicle.models import Vehicle

fake = Faker(["en_US"])


def add_bulk_driver() -> None:
    drivers = []
    for i in range(10000):
        license_number = generate_license_number()
        name = fake.first_name()
        personal_id = generate_personal_id()
        try:
            driver = Driver(name=name, personal_id=personal_id, license_number=license_number)
            drivers.append(driver)
            print("add driver -> ", i)
        except Exception as e:
            print("set_driver err", e)

    Driver.objects.bulk_create(drivers)


def add_driver() -> Driver:
    name = fake.first_name()
    license_number = generate_license_number()
    personal_id = generate_personal_id()
    driver = Driver.objects.create(name=name, personal_id=personal_id, license_number=license_number)
    print("driver: ", driver)
    return driver


def add_location() -> Location:
    names = ["Bakırkoy-incirli", "Güneşli-YeniBosna", "Bağcılar-Bakırköy", "Küçükçekmece-Aksaray", "Kadıköy-Ümraniye"]
    name = random.choice(names)
    latitude = fake.latitude()
    longitude = fake.longitude()
    location = Location.objects.create(name=name, latitude=latitude, longitude=longitude)
    return location


def add_vehicle(driver: Driver) -> Vehicle:
    models = ["Mercedes", "Man", "OTOKAR"]
    is_actives = [True, False]
    license_plate = generate_license_plate()
    model = random.choice(models)
    is_active = random.choice(is_actives)
    vehicle = Vehicle.objects.create(license_plate=license_plate, model=model, driver=driver, is_active=is_active)
    print("vehicle ", vehicle)
    return vehicle


def generate_personal_id() -> str:
    while True:
        personal_id = fake.random_number(digits=11, fix_len=True)
        if not Driver.objects.filter(personal_id=personal_id).exists():
            return str(personal_id)


def generate_license_plate() -> str:
    while True:
        license_plate = fake.license_plate()
        if not Vehicle.objects.filter(license_plate=license_plate).exists():
            return str(license_plate)


def generate_license_number() -> str:
    while True:
        license_number = fake.random_number(digits=20, fix_len=True)
        if not Driver.objects.filter(license_number=license_number).exists():
            return str(license_number)


def create_vehicle():
    driver = add_driver()
    vehicle = add_vehicle(driver)
    location = add_location()
    vehicle.locations.add(location)


def main():
    for i in range(10000):
        create_vehicle()


main()
