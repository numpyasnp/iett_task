from django.db import models
from django.db.models import QuerySet

from libs.models.abstract import TimestampedModel


class VehicleQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)


class Vehicle(TimestampedModel):
    license_plate = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    make = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField()
    driver = models.ForeignKey("driver.Driver", related_name="vehicles", on_delete=models.CASCADE)
    location = models.ForeignKey("location.Location", null=True, related_name="vehicles", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    objects = models.manager.QuerySet()
