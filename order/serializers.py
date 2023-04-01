from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "number_order",
            "amount",
            "weight",
            "width",
            "height",
            "length",
            "zip_from",
            "zip_to",
        ]
