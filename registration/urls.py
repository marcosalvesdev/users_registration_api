from rest_framework import routers
from django.urls import path, include
from .views import UserRegistration, AdressRegistration

app_name = "registration"

router = routers.DefaultRouter()

# USER URLS #
urlpatterns = [
    path('', include(router.urls)),
    path('regiser_user/', UserRegistration.as_view({'post': 'create'}), name='regiser_user'),
    path('list_user/', UserRegistration.as_view({'get': 'list'}), name='list_user'),
    path('filter_in_user/', AdressRegistration.as_view({'post': 'filter_in_user'}), name='filter_in_user'),
    path('retrieve_user/<str:pk>', UserRegistration.as_view({'get': 'retrieve'}), name='retrieve_user'),
    path('update_user/<str:pk>', UserRegistration.as_view({'put': 'update'}), name='retrieve_user'),
    path('delete_user/<str:pk>', UserRegistration.as_view({'delete': 'destroy'}), name='destroy_user')
]

# ADRESS URLS #
urlpatterns += [
    path('register_adress/', AdressRegistration.as_view({'post': 'create'}), name='register_adress'),
    path('list_adress/', AdressRegistration.as_view({'get': 'list'}), name='list_adress'),
    path('filter_in_adress/', AdressRegistration.as_view({'post': 'filter_in_adress'}), name='filter_in_adress'),
    path('retrieve_adress/<str:pk>', AdressRegistration.as_view({'get': 'retrieve'}), name='retrieve_adress'),
    path('update_adress/<str:pk>', AdressRegistration.as_view({'put': 'update'}), name='update_adress'),
    path('delete_adress/<str:pk>', AdressRegistration.as_view({'delete': 'destroy'}), name='delete_adress')
]
