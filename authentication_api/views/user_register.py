from authentication_api.serializer import RegisterUserSerializer
from authentication_api.models import ApiUser
from rest_framework import viewsets


class RegisterNewUser(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = RegisterUserSerializer
