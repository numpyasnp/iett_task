from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import DriverSerializer
from driver.models import Driver
from rest_framework_simplejwt.authentication import JWTAuthentication


class DriverSearchPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 250


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.select_related("user").all()
    serializer_class = DriverSerializer
    pagination_class = DriverSearchPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = (filters.SearchFilter,)
    search_fields = ["license_number", "user__name"]

    @extend_schema(
        summary="List all drivers",
        description="Returns a list of all drivers in the database.",
        responses={200: DriverSerializer},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
