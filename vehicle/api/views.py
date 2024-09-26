from rest_framework import generics

from driver.api.serializers import VehicleSerializer
from vehicle.models import Vehicle
from rest_framework.pagination import LimitOffsetPagination


class SearchVehicleView(LimitOffsetPagination):
    default_limit = 50
    max_limit = 250


class VehicleViewSet(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    pagination_class = LimitOffsetPagination
    search_fields = ""
