from .models import ApiUser, ApiUserManager
from rest_framework import serializers
from rest_framework.status import HTTP_400_BAD_REQUEST


# Register serializer class
class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = ApiUser
        fields = ['email', 'username', 'password', 'password2', 'is_admin']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}},
        }

    def save(self):
        acount = ApiUser(
            email=self.validated_data['email'],
            id=self.validated_data['username'],
            username=self.validated_data['username'],
            is_admin=self.validated_data['is_admin'],
            is_superuser=self.validated_data['is_admin'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        try:
            assert password == password2
            acount.set_password(password)
            acount.save()
        except AssertionError:
            raise serializers.ValidationError(
                {'password': 'Passwords must match!',
                 'HTTP_STATUS': HTTP_400_BAD_REQUEST}
            )
        else:
            return acount


class LogingUserSerializer(serializers.ModelSerializer):
    pass
