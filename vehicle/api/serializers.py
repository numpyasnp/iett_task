from rest_framework import serializers

from location.api.serializers import LocationSerializer
from vehicle.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = ["license_plate", "model", "locations"]
