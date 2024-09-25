from django.db import models


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    make = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField()
    driver = models.ForeignKey("driver.Driver", related_name="vehicles", on_delete=models.CASCADE)
    location = models.ForeignKey("location.Location", null=True, related_name="vehicles", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
