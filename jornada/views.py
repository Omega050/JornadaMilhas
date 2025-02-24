import django_filters
from rest_framework import viewsets, filters
from jornada.models import Depoimento, Destino
from .serializers import DepoimentoSerializer, DestinoSimplificadoSerializer, DestinoDetalhadoSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

class DepoimentoViewSet(viewsets.ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer

class DestinoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')  # Busca parcial, case-insensitive

    class Meta:
        model = Destino
        fields = ['nome']

class DestinoSimplificadoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSimplificadoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = DestinoFilter
    ordering_fields = ['nome']

class DestinoDetalhadoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoDetalhadoSerializer

class ListaDepoimentosAleatorios(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        queryset = Depoimento.objects.order_by('?')[:3]
        return queryset
    serializer_class = DepoimentoSerializer