from django.db import models
import uuid


class Freight(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    carrier = models.CharField(max_length=64, blank=True, null=True)
    delivery_time = models.CharField(max_length=64, blank=True, null=True)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2)
    external_freight_id = models.IntegerField()
    ensurance_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order = models.ForeignKey(
        "order.Order", related_name="freights", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.carrier} - R${self.delivery_cost} - {self.delivery_time}"
