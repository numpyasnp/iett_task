from django.urls import path, include
from .views import DriverViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"drivers", DriverViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
