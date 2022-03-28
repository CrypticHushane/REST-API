from dataclasses import field, fields
from re import M
from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["title","description","price"]


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.League
        fields = ["name", "numOfTeams"]

class FootballClubSerializer(serializers.ModelSerializer):
    league = serializers.PrimaryKeyRelatedField(queryset = models.League.objects.all())

    class Meta:
        model = models.FootballClub
        fields = ['name','numOfPlayers', 'league']