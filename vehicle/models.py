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
    year = models.IntegerField(null=True)
    driver = models.ForeignKey("driver.Driver", related_name="vehicles", on_delete=models.CASCADE, null=True)
    locations = models.ManyToManyField("location.Location", related_name="vehicles")
    is_active = models.BooleanField(default=True)

    objects = VehicleQuerySet.as_manager()

    @property
    def has_location(self):
        return self.locations is not None


# TODO: redis
