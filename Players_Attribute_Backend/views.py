"""
Create views for Players_Attribute_Backend project.
"""

# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Country, Club, Player
from .serializer import CountrySerializer, ClubSerializer, PlayerSerializer
from .data.fixed_data import FixedData

F_DATA = FixedData()



@api_view(['GET'])
def get_players_list(request):
    # handle path: api/
    app = Player.objects.all()
    serializer = PlayerSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_list(request):
    # handle path: api/countries/
    app = Country.objects.all()
    serializer = CountrySerializer(app, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_club_list(request):
    # handle path: api/clubs/
    app = Club.objects.all()
    serializer = ClubSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_attribute_list(request):
    # handle path: api/attributes/
    return Response(F_DATA.attributes)


@api_view(['GET'])
def get_player_detail(request, slug):
    # handle path: api/players/<slug:slug>/
    app = Player.objects.filter(slug=slug)
    serializer = PlayerSerializer(app, many=True)
    return Response(serializer.data)

