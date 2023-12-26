"""
Serializers created for models in Players_Attribute_Backend project.
"""

from rest_framework import serializers
from .models import Country, Club, Player
from .data.fixed_data import FixedData

F_DATA = FixedData()


class CountrySerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['name', 'players']


class ClubSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True, read_only=True, )
    class Meta:
        model = Club
        fields = ['name', 'players']


class PlayerSerializer(serializers.ModelSerializer):
    Nationality = serializers.StringRelatedField(many=True)
    Club = serializers.StringRelatedField(many=True)
    class Meta:
        model = Player
        fields = F_DATA.attributes
