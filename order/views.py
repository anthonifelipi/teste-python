from django.shortcuts import render
from django.core import exceptions
from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.views import Request, Response, status
from .serializers import OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()
