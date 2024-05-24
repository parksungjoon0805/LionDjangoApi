from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Profile
from apiset.serializers import ProductSerializer, ProfileSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer