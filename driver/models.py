from django.db import models
from django.db.models import QuerySet

from libs.models.abstract import TimestampedModel


class DriverQuerySet(QuerySet):
    def has_phone_number(self):
        return self.filter(phone_number__isnull=False)

    def active(self):
        return self.filter(is_active=True)


class Driver(TimestampedModel):
    name = models.CharField(max_length=255)
    personal_id = models.CharField(max_length=11, unique=True)
    license_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    objects = DriverQuerySet().as_manager()

    def get_username(self):
        return self.name
