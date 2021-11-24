from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Adress
from .serializer import UserSerializer, AdressSerializer, FilterEspcFieldSerializer
from .aux_functions import CpfAuxMethods, CepAuxMethods, Filter
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .swagger_params import SwaggerFields

"""This variable below was created for to be used with Swagger"""


class UserRegistration(viewsets.ModelViewSet):
    get_one_field = Filter
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    swagger_fields = SwaggerFields()

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def create(self, request, *args, **kwargs):
        try:
            assert len(request.data) != 0
            cpf = request.data.get('cpf')
            valid = CpfAuxMethods.cpf_verificator(cpf)
            if valid is True:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'message': valid[1]}, status=status.HTTP_400_BAD_REQUEST)
        except AssertionError:
            return Response({'message': "Don't send a empty request", 'HTTP_STATUS': 204},
                            status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        manual_parameters=[swagger_fields.authorization_field()],
        request_body=swagger_fields.user_fields(),
    )
    def filter_in_users(self, request):
        try:
            assert len(request.data) != 0
            init_class = self.get_one_field(request=request, serializer_class=FilterEspcFieldSerializer, model=User)
            response = init_class.filter()
            return Response(response)
        except AssertionError:
            return Response({'message': "Don't send a empty request", 'HTTP_STATUS': 204},
                            status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def update(self, request, *args, **kwargs):
        try:
            assert len(request.data) != 0
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        except AssertionError:
            return Response({'message': "Don't send a empty request", 'HTTP_STATUS': 204},
                            status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdressRegistration(viewsets.ModelViewSet):
    get_one_field = Filter
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer
    permission_classes = [IsAuthenticated]
    swagger_fields = SwaggerFields()

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def create(self, request, *args, **kwargs):
        try:
            assert len(request.data) != 0
            cep = request.data.get('cep')
            instance = CepAuxMethods(cep)
            valid_cep = instance.cep_validation()
            if valid_cep[0] is True:
                request.data['cep'] = valid_cep[1]
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'message': valid_cep[1]}, status=status.HTTP_400_BAD_REQUEST)
        except AssertionError:
            return Response({'message': "Don't send a empty request", 'HTTP_STATUS': 204},
                            status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()],
                         request_body=swagger_fields.adress_fields())
    # TODO: APERFEIÇOAR ESSE MÉTODO NO SWAGGER
    def filter_in_adress(self, request):
        try:
            assert len(request.data) != 0
            init_class = self.get_one_field(request=request, serializer_class=FilterEspcFieldSerializer, model=Adress)
            response = init_class.filter()
            print(response)
            return Response(response)
        except AssertionError:
            return Response({'message': "Don't send a empty request", 'HTTP_STATUS': 204}, )

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def update(self, request, *args, **kwargs):
        try:
            assert len(request.data) != 0
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        except AssertionError:
            return Response({'message': "Don't send a empty request", 'HTTP_STATUS': 204},
                            status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(manual_parameters=[swagger_fields.authorization_field()])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
