import django
django.setup()
from registration.serializer import FilterEspcFieldSerializer
from registration.models import GenericModelForSwaggerFilds
from drf_yasg import openapi

"""This module has the fields for swagger documentation."""


class SwaggerFields:
    @staticmethod
    def authorization_field():
        # Fields to be used in the HEAD #
        token_field = openapi.Parameter(
            'Authorization',
            in_=openapi.IN_HEADER,
            description='Description',
            type=openapi.TYPE_STRING,
            required=True,
        )
        return token_field

    @staticmethod
    def user_fields():
        serializer = FilterEspcFieldSerializer
        serializer.Meta.model = GenericModelForSwaggerFilds
        serializer.Meta.fields = ['user_id', 'field']
        return serializer

    @staticmethod
    def adress_fields():
        serializer = FilterEspcFieldSerializer
        serializer.Meta.model = GenericModelForSwaggerFilds
        serializer.Meta.fields = ['user_id', 'field']
        return serializer


if __name__ == '__main__':
    ...
