from rest_framework import serializers

from jornada.models import Depoimento

class DepoimentoSerializer(serializers.ModelSerializer):
    model = Depoimento
    fields = '__all__'