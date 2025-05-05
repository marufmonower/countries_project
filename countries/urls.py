from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CountryViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]