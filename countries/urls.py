from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CountryViewSet
from .import views

router = DefaultRouter()
router.register(r'countries', CountryViewSet,basename='country')

urlpatterns = [
    path('api/', include(router.urls)),
    path('countries/',views.country_list,name = 'country_list'),
    path('countries/<int:pk>/details/',views.country_details,name = 'country_details'),
]