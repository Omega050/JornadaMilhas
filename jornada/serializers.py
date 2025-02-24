from rest_framework import serializers

from jornada.models import Depoimento, Destino

class DepoimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = '__all__'

class DestinoSimplificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'nome', 'imagem', 'preco']

class DestinoDetalhadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

