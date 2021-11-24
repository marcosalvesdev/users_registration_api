from rest_framework import serializers
from .models import User, Adress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = [
            'cep',
            'street',
            'house_number',
            'state',
            'city',
            'user',
        ]


class FilterEspcFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = object
        fields = None
