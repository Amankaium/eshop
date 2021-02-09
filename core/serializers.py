from rest_framework import serializers 
from .models import *


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ["name", "price", "qty"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["description", "phone_number", ]

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

