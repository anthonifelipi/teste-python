from django.test import TestCase

from order.models import Order
from freight.models import Freight


class OrderTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.order_test = {
            "number_order": 1,
            "amount": 22,
            "weight": 10.00,
            "width": 10.90,
            "height": 17.00,
            "length": 13.99,
            "zip_from": 11430360,
            "zip_to": 11430000,
            "courier_choice": "SEDEX",
        }

        cls.freight_test = {
            "carrier": "SEDEX",
            "delivery_time": 5,
            "delivery_cost": 38.00,
            "external_freight_id": 1,
            "ensurance_price": 100,
        }

        cls.order = Order.objects.create(**cls.order_test)

        cls.freight = Freight.objects.create(
            **cls.freight_test,
            order_id=cls.order.id,
        )

    def test_order_fields(self):
        self.assertEqual(self.order.number_order, self.order_test["number_order"])
        self.assertEqual(self.order.amount, self.order_test["amount"])
        self.assertEqual(self.order.weight, self.order_test["weight"])
        self.assertEqual(self.order.width, self.order_test["width"])
        self.assertEqual(self.order.height, self.order_test["height"])
        self.assertEqual(self.order.length, self.order_test["length"])
        self.assertEqual(self.order.zip_from, self.order_test["zip_from"])
        self.assertEqual(self.order.zip_to, self.order_test["zip_to"])
        self.assertEqual(self.order.courier_choice, "SEDEX")

    def test_freight_fields(self):
        self.assertEqual(self.freight.carrier, self.freight_test["carrier"])
        self.assertEqual(self.freight.delivery_time, self.freight_test["delivery_time"])
        self.assertEqual(self.freight.delivery_cost, self.freight_test["delivery_cost"])
        self.assertEqual(
            self.freight.external_freight_id, self.freight_test["external_freight_id"]
        )
        self.assertEqual(
            self.freight.ensurance_price, self.freight_test["ensurance_price"]
        )

    def test_relation_order_freight(self):
        self.assertEqual(self.order.id, self.freight.order_id)
