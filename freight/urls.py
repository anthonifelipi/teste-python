from django.urls import path
from . import views


urlpatterns = [
    path("freight/", views.OrderCreateView.as_view(), name="freight"),
]
