from rest_framework.serializers import ModelSerializer
from main.models import *


class WaterSerializer(ModelSerializer):
    class Meta:
        model = Water
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
