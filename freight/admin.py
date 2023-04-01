from django.contrib import admin
from .models import Freight


class FreightAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "carrier",
        "delivery_time",
        "delivery_cost",
        "ensurance_price"
    ]
    list_filter = ["carrier"]
    search_fields = ["order_number"]


admin.site.register(
    Freight,
    FreightAdmin,
)
