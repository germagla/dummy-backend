from rest_framework import serializers
from .models import City


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'current_time', 'time_offset',)
