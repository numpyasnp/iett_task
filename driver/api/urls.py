from django.urls import path, include
from .views import DriverViewSet
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()
router_v1.register(r"v1", DriverViewSet)

urlpatterns = [
    path("api/", include(router_v1.urls)),
]
