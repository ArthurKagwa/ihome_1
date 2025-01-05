from django.urls import path, include
from rest_framework import routers
from .views import AnimalViewSet, BreedViewSet, TypeViewSet, StaffViewSet

router = routers.DefaultRouter()
router.register('animals', AnimalViewSet)
router.register('breeds', BreedViewSet)
router.register('types', TypeViewSet)
router.register('staff', StaffViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include the router's URLs
]