from rest_framework import serializers
from driver.models import Driver
from vehicle.api.serializers import VehicleSerializer


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ["pk", "name", "personal_id", "license_number", "phone_number", "is_active"]


class DriverVehicleSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ["name", "personal_id", "license_number", "phone_number", "is_active", "vehicles"]
