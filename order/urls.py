from django.urls import path
from . import views


urlpatterns = [
    path("order/", views.OrderCreateView.as_view(), name="order"),
]
