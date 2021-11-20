from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Adress
from .serializer import UserSerializer, AdressSerializer, FilterEspcField
from .aux_functions import CpfAuxMethods, CepAuxMethods, Filter
from rest_framework.permissions import IsAuthenticated


class UserRegistration(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    get_one_field = Filter

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

    def filter_in_users(self, request):
        init_class = self.get_one_field(request=request, serializer_class=FilterEspcField, model=Adress)
        response = init_class.filter()
        return Response(response)



class AdressRegistration(viewsets.ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer
    permission_classes = [IsAuthenticated]
    get_one_field = Filter

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


    def filter_in_adress(self, request):
        init_class = self.get_one_field(request=request, serializer_class=FilterEspcField, model=Adress)
        response = init_class.filter()
        return Response(response)



