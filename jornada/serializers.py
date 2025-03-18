from rest_framework import serializers
from jornada.validators import nome_invalido, preco_invalido
from jornada.models import Depoimento, Destino

class DepoimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = '__all__'
    
    def validate(self,dados):
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        return dados

class DestinoSimplificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'nome', 'imagem', 'preco']

class DestinoDetalhadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'
    
    def validate(self,dados):
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if preco_invalido(dados['preco']):
            raise serializers.ValidationError({'preco':'O preço mínimo de um destino deve ser 100 BRL e o máximo de 30000 BRL'})
        return dados
