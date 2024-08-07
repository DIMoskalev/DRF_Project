from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet

app_name = VehicleConfig.name

router = DefaultRouter()
router.register('cars', CarViewSet, basename='cars')

urlpatterns = [

] + router.urls
