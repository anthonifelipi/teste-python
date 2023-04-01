from django.contrib import admin
from django.utils.translation import gettext_lazy as lazy

from .models import Order
from freight.models import Freight
from .utils import calculate_freight


class FreightInline(admin.StackedInline):
    model = Freight
    extra = 1
    readonly_fields = [
        "delivery_cost",
        "delivery_time",
        "external_freight_id",
        "carrier",
    ]


class Order_Admin(admin.ModelAdmin):
    inlines = [FreightInline]
    search_fields = ["number_order"]
    list_display = (
        "number_order",
        "amount",
        "weight",
        "width",
        "height",
        "length",
        "zip_from",
        "zip_to",
        "courier_choice",
    )
    list_editable = [
        "courier_choice",
        "amount",
        "weight",
        "width",
        "height",
        "length",
        "zip_from",
        "zip_to",
    ]

    def calculate_freight_action(self, request, queryset):
        for item in queryset:
            freight_data = calculate_freight(item)
            print(freight_data)
            if freight_data:
                freight = Freight.objects.create(**freight_data)
                self.message_user(
                    request, f"Freight calculated for order{item.number_order}"
                )
            else:
                self.message_user(
                    request,
                    f"Error calculating freight for order {item.number_order}",
                    level="ERROR",
                )

    calculate_freight_action.short_description = lazy("Calcular frete")
    actions = [calculate_freight_action]


admin.site.register(Order, Order_Admin)
