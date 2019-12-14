from rest_framework_json_api import serializers as json_api_serializers
from rest_framework import serializers
from .models import Control

class ControlSerializer(json_api_serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'

class ControlCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ['name', 'type', 'maximum_rabi_rate', 'polar_angle']
