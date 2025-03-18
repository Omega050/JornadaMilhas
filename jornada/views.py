import django_filters
from rest_framework import viewsets, filters, serializers
from jornada.models import Depoimento, Destino
from .serializers import DepoimentoSerializer, DestinoSimplificadoSerializer, DestinoDetalhadoSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.exceptions import NotFound
from .permissions import VerificarSuperUsuario

class DepoimentoViewSet(viewsets.ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
    
    #Permissions
    permission_classes = (VerificarSuperUsuario, permissions.DjangoModelPermissions,)

class DestinoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')  # Busca parcial, case-insensitive

    class Meta:
        model = Destino
        fields = ['nome']

class DestinoSimplificadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSimplificadoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = DestinoFilter
    ordering_fields = ['nome']

    def get_object(self):
        try:
            return super().get_object()
        except NotFound:
            raise NotFound({'Mensagem':'Destino não encontrado'})

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response(
                {"mensagem": "Nenhum destino encontrado."}, 
                status=status.HTTP_404_NOT_FOUND
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class DestinoDetalhadoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoDetalhadoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response(
                {"mensagem": "Nenhum destino encontrado."}, 
                status=status.HTTP_404_NOT_FOUND
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    #Permissions
    permission_classes = (VerificarSuperUsuario, permissions.DjangoModelPermissions,)


class ListaDepoimentosAleatorios(viewsets.ReadOnlyModelViewSet):
    
    def get_queryset(self):
        queryset = Depoimento.objects.order_by('?')[:3]
        return queryset
    
    serializer_class = DepoimentoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response(
                {"mensagem": "Nenhum depoimento encontrado."}, 
                status=status.HTTP_404_NOT_FOUND
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)