from django.urls import path
from .views.user_register import RegisterNewUser


app_name = "authentication_api"

urlpatterns = [
    path('create_user/', RegisterNewUser.as_view({'post': 'create'}), name='create_user')
]
