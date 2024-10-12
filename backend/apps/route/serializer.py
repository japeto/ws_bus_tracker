from rest_framework import serializers
from .models import Route, Station, RouteStation

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'name', 'description']

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'latitude', 'longitude']

class RouteStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteStation
        fields = ['id', 'route', 'station', 'order']
