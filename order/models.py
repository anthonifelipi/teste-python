from django.db import models
import uuid


class Currier(models.TextChoices):
    PAC = "1"
    SEDEX = "2"
    JADLOG_Package = "3"
    JADLOG_COM = "4"


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    number_order = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    zip_from = models.IntegerField()
    zip_to = models.IntegerField()
    courier_choice = models.CharField(
        max_length=15,
        choices=Currier.choices,
        default=Currier.PAC,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
