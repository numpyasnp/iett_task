from rest_framework import viewsets

from driver.api.serializers import LocationSerializer
from location.models import Location


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
