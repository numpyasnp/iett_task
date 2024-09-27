from .serializers import UserSerializer
from user.models import User

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication


class UserSearchPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 250


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related("driver").all()
    serializer_class = UserSerializer
    pagination_class = UserSearchPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name", "personal_id"]

    @extend_schema(
        summary="List all User",
        description="Returns a list of all Users in the database.",
        responses={200: UserSerializer},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
