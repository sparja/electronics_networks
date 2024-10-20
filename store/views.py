from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError

from store.models import NetworkEntity, Product
from store.permissions import IsActiveUserPermissions
from store.serializers import NetworkEntitySerializers, ProductSerializers


class NetworkEntityCreateAPIView(generics.CreateAPIView):
    '''Класс создания сети'''
    serializer_class = NetworkEntitySerializers
    permission_classes = [IsActiveUserPermissions]


class NetworkEntityListAPIView(generics.ListAPIView):
    ''' Класс просмотра магазинов '''
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country',)
    permission_classes = [IsActiveUserPermissions]


class NetworkEntityRetrieveAPIView(generics.RetrieveAPIView):
    ''' Класс просмотра одного магазина '''
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()
    permission_classes = [IsActiveUserPermissions]


class NetworkEntityUpdateAPIView(generics.UpdateAPIView):
    ''' Класс обновления магазина '''
    serializer_class = NetworkEntitySerializers
    queryset = NetworkEntity.objects.all()
    permission_classes = [IsActiveUserPermissions]

    def perform_update(self, serializer):
        if 'debt' in serializer.validated_data:
            serializer.validated_data.pop('debt')
            raise ValidationError('У вас нет прав менять задолность')
        super().perform_update(serializer)


class NetworkEntityDestroyAPIView(generics.DestroyAPIView):
    ''' Класс удаления магазина '''
    queryset = NetworkEntity.objects.all()
    permission_classes = [IsActiveUserPermissions]


class ProductViewSet(viewsets.ModelViewSet):
    '''вьюсет для продуктов'''
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsActiveUserPermissions]
