from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
