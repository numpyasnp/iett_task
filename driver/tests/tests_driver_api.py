# Create your tests here.
from django.contrib.auth.models import User

from model_bakery import baker
from rest_framework.test import APITestCase
from django.urls import reverse

from driver.models import Driver


class DriverApiTest(APITestCase):

    def setUp(self):
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
        driver = baker.make("driver.Driver")
        url = reverse("driver-detail", kwargs={"pk": driver.pk})

        # When
        response = self.client.get(url)

        # Then
        self.assertEquals(response.status_code, 200)

    def test_create_driver(self):
        # Given
        url = reverse("driver-list")
        user = baker.make("user.User")
        data = {"user": user.pk, "license_number": "123456789"}

        # When
        response = self.client.post(url, data=data, format="json")

        # Then
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Driver.objects.count(), 1)
        driver = Driver.objects.first()
        self.assertEquals(driver.license_number, data["license_number"])
        self.assertEquals(driver.user_id, data["user"])

    def test_update_driver(self):
        # Given
        license_number = "1900"
        user = baker.make("user.User")
        driver = baker.make("driver.Driver", license_number=license_number, user=user)
        url = reverse("driver-detail", kwargs={"pk": driver.pk})
        new_data = {"license_number": "1991", "user": user.pk, "phone_number": "+905551112233"}
        self.assertEquals(driver.license_number, license_number)
        self.assertEquals(driver.user, user)
        self.assertEquals(driver.phone_number, None)

        # When
        response = self.client.put(url, new_data, format="json")

        # Then
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data["license_number"], new_data["license_number"])
        self.assertEquals(response.data["user"], new_data["user"])
        self.assertEquals(response.data["phone_number"], new_data["phone_number"])

    def test_destroy_driver(self):
        # Given
        user = baker.make("user.User")
        driver = baker.make("driver.Driver", license_number="1900", user=user)
        url = reverse("driver-detail", kwargs={"pk": driver.pk})

        self.assertEquals(Driver.objects.count(), 1)

        # When
        response = self.client.delete(url, format="json")

        # Then
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Driver.objects.count(), 0)
