from rest_framework import serializers
from .models import Bus, Location

class BusSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Bus
    fields = '__all__'
    
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'updated_at']