from django.contrib.auth.models import User
from django.core.cache import cache
from model_bakery import baker
from rest_framework.test import APITestCase
from django.urls import reverse

from driver.models import Driver
from driver.tests.mixins import BaseDriverMixin


class DriverApiTest(APITestCase, BaseDriverMixin):

    def setUp(self):
        cache.clear()
        self.username = "admin"
        self.password = "test123."
        User.objects.create_superuser(username=self.username, password=self.password)
        access_token_url = reverse("token_obtain_pair")
        user_credentials = {"username": self.username, "password": self.password}
        response = self.client.post(access_token_url, user_credentials, format="json").json()
        self.access_token = response.get("access", None)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

    def test_unauthorized_api_call(self):
        # Given
        self.client.credentials()
        url = reverse("driver-list")

        # When
        response = self.client.get(url)

        # Then
        self.assertEquals(response.status_code, 401)

    def test_get_driver_list(self):
        # Given
        url = reverse("driver-list")

        # When
        response = self.client.get(url)

        # Then
        self.assertEquals(response.status_code, 200)

    def test_get_driver_details(self):
        # Given
        driver = self.create_driver()
        url = reverse("driver-detail", kwargs={"pk": driver.pk})

        # When
        response = self.client.get(url)

        # Then
        self.assertEquals(response.status_code, 200)

    def test_create_driver(self):
        # Given
        url = reverse("driver-list")
        data = {"license_number": "123456789", "name": "ugurcan", "personal_id": "123"}

        # When
        response = self.client.post(url, data=data, format="json")

        # Then
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Driver.objects.count(), 1)
        driver = Driver.objects.first()
        self.assertEquals(driver.license_number, data["license_number"])

    def test_update_driver(self):
        # Given
        license_number, personal_id, name, phone_number = "111", "222", "Ugurcan", "+905523336677"
        driver = self.create_driver(personal_id, license_number, name, phone_number)
        url = reverse("driver-detail", kwargs={"pk": driver.pk})
        new_data = {
            "license_number": "1991",
            "phone_number": "+905551112233",
            "name": "lorem ipsum",
            "personal_id": "234",
        }
        self.assertEquals(driver.license_number, license_number)
        self.assertEquals(driver.name, name)
        self.assertEquals(driver.personal_id, personal_id)
        self.assertEquals(driver.phone_number, phone_number)

        # When
        response = self.client.put(url, new_data, format="json")

        # Then
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data["license_number"], new_data["license_number"])
        self.assertEquals(response.data["phone_number"], new_data["phone_number"])
        self.assertEquals(response.data["name"], new_data["name"])
        self.assertEquals(response.data["personal_id"], new_data["personal_id"])

    def test_destroy_driver(self):
        # Given
        driver = self.create_driver()
        url = reverse("driver-detail", kwargs={"pk": driver.pk})

        self.assertEquals(Driver.objects.count(), 1)

        # When
        response = self.client.delete(url, format="json")

        # Then
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Driver.objects.count(), 0)

    def test_driver_active_vehicle(self):
        # Given
        driver = self.create_driver()
        license_plate, model = "34IETT34", "OTOKAR"
        url = reverse("user-vehicle-list", kwargs={"pk": driver.pk})
        baker.make("vehicle.Vehicle", driver=driver, license_plate=license_plate, model=model)
        expected_response = {
            "name": "John Doe",
            "personal_id": "123",
            "license_number": "456",
            "phone_number": "+905553331122",
            "is_active": True,
            "vehicles": [{"license_plate": license_plate, "model": model, "locations": []}],
        }
        # When
        response = self.client.get(url)

        # Then
        self.assertEquals(response.data, expected_response)
