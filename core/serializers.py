from rest_framework import serializers 
from .models import *


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ["name", "price", "qty"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["description", "phone_number"]
