from rest_framework import viewsets
from jornada.models import Depoimento
from .serializers import DepoimentoSerializer

class DepoimentoViewSet(viewsets.ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer

class ListaDepoimentosAleatorios(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        queryset = Depoimento.objects.order_by('?')[:3]
        return queryset
    serializer_class = DepoimentoSerializer