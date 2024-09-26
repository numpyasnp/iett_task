from django.db import models
from django.utils import timezone

from libs.models.abstract import TimestampedModel


class Location(TimestampedModel):
    vehicle = models.ForeignKey("vehicle.Vehicle", related_name="locations", on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.vehicle.license_plate} at {self.latitude}, {self.longitude} on {self.timestamp}"
