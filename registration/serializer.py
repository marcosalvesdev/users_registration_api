from rest_framework import serializers
from .models import User, Adress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdressSerializer(serializers.ModelSerializer):
    def __init__(self, field, **kwargs):
        super().__init__(**kwargs)
        self.field = field

    def field(self):
        return self.field()

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


class FilterEspcField(serializers.ModelSerializer):

    class Meta:
        model = object
        fields = []
