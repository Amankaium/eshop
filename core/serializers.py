from rest_framework import serializers 
from .models import *


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ["name", "price", "qty"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["description", "phone_number", "user"]

# class AllSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = All
#         fields = [
#         "name", "price", "qty",
#         "description", "phone_number", "user"
#         ]
