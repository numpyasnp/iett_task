from django.db import models

from libs.models.abstract import TimestampedModel


class Driver(TimestampedModel):
    user = models.OneToOneField("user.User", related_name="driver", on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
