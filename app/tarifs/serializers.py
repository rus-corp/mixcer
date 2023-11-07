from rest_framework import serializers

from .models import UserTarif, Tarif
from app.content.models import Content





class TarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = ['id', 'name', 'desc', 'price', 'shot_count',]
        # read_only_fields = ['', '',]


class ContentTarifSerializer(serializers.ModelSerializer):
    tarif = TarifSerializer(many=True, source='tarifs')
    class Meta:
        model = Content
        fields = ['id', 'name', 'tarif']
        read_only_fields = ['name',]




class UserTarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTarif
        fields = ['tarif', 'user', 'shot_remains']
        read_only_fields = ['user', 'shot_remains']
        
    def create(self, validated_data):
        tarif_data = validated_data.pop('tarif')
        shot_remains = tarif_data.shot_count
        validated_data['shot_remains'] = shot_remains
        user_tarif = UserTarif.objects.create(tarif=tarif_data, **validated_data)
        return user_tarif
        



class ListUserTarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTarif
        fields = ['id', 'tarif', 'shot_remains']
        read_only_fields = ['user',]