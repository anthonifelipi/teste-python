from rest_framework import serializers
from .models import Freight


class FreightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freight
        fields = [
            "id",
            "carrier",
            "delivery_time",
            "delivery_cost",
            "external_freight_id",
            "order",
        ]
