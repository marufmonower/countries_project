from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CountryViewSet
from .import views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'countries', CountryViewSet,basename='country')

urlpatterns = [
    path('api/', include(router.urls)),
    path('countries/',views.country_list,name = 'country_list'),
    path('countries/<int:pk>/details/',views.country_details,name = 'country_details'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',next_page = 'country_list'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]