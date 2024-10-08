from django.conf import settings
from django.core.cache import cache
from django.db.models import Prefetch
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from libs.api.authentication.mixins import JWTIsAuthenticatedMixin
from .serializers import DriverSerializer, DriverVehicleSerializer
from driver.models import Driver


class DriverSearchPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 250


class DriverViewSet(viewsets.ModelViewSet, JWTIsAuthenticatedMixin):
    queryset = Driver.objects.prefetch_related("vehicles").all()
    serializer_class = DriverSerializer
    pagination_class = DriverSearchPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ["license_number", "name", "personal_id"]

    @extend_schema(
        summary="List all drivers",
        description="Returns a list of all drivers in the database.",
        responses={200: DriverSerializer},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DriverActiveVehicleViewSet(viewsets.ViewSet, JWTIsAuthenticatedMixin):
    BASE_CACHE_KEY = "driver_vehicles"

    @extend_schema(
        summary="List all vehicle of Drivers",
        description="Returns a list of vehicle of drivers in the database.",
        responses={200: DriverSerializer},
    )
    def retrieve(self, request, pk=None):
        cache_key = self.BASE_CACHE_KEY + "_" + str(pk)
        if cached_data := cache.get(cache_key):
            print("data from cache")
            return Response(cached_data)

        try:
            location_prefetch = Prefetch("vehicles__locations")
            driver = Driver.objects.active().prefetch_related("vehicles", location_prefetch).get(pk=pk)
        except Driver.DoesNotExist:
            return Response({"detail": "Driver not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverVehicleSerializer(driver)

        cache.set(cache_key, serializer.data, timeout=settings.DRIVER_VEHICLE_CACHE_TTL)

        return Response(serializer.data, status=status.HTTP_200_OK)
