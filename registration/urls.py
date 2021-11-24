from rest_framework import routers
from django.urls import path, include
from .views import UserRegistration, AdressRegistration

app_name = "registration"

router = routers.DefaultRouter()

# USER URLS #
urlpatterns = [
    path('', include(router.urls)),
    path('register_a_user/', UserRegistration.as_view({'post': 'create'}), name='regiser_user'),
    path('list_all_users/', UserRegistration.as_view({'get': 'list'}), name='list_user'),
    path('filter_in_user/', UserRegistration.as_view({'post': 'filter_in_users'}), name='filter_in_users'),
    path('retrieve_a_user/<str:pk>', UserRegistration.as_view({'get': 'retrieve'}), name='retrieve_user'),
    path('update_a_user/<str:pk>', UserRegistration.as_view({'put': 'update'}), name='retrieve_user'),
    path('delete_a_user/<str:pk>', UserRegistration.as_view({'delete': 'destroy'}), name='destroy_user')
]

# ADRESS URLS #
urlpatterns += [
    path('register_an_adress/', AdressRegistration.as_view({'post': 'create'}), name='register_adress'),
    path('list_all_adresses/', AdressRegistration.as_view({'get': 'list'}), name='list_adress'),
    path('filter_in_adress/', AdressRegistration.as_view({'post': 'filter_in_adress'}), name='filter_in_adress'),
    path('retrieve_an_adress/<str:pk>', AdressRegistration.as_view({'get': 'retrieve'}), name='retrieve_adress'),
    path('update_an_adress/<str:pk>', AdressRegistration.as_view({'put': 'update'}), name='update_adress'),
    path('delete_an_adress/<str:pk>', AdressRegistration.as_view({'delete': 'destroy'}), name='delete_adress')
]


