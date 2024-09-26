from django.db import models
from django.db.models import QuerySet

from libs.models.abstract import TimestampedModel


class DriverQuerySet(QuerySet):
    def has_phone_number(self):
        return self.filter(phone_number__isnull=False)


class Driver(TimestampedModel):
    user = models.OneToOneField("user.User", related_name="driver", on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    objects = DriverQuerySet().as_manager()
