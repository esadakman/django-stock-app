from django.shortcuts import render
from rest_framework import viewsets
from .models import Brand, Category, Product, Firm
from .serializers import CategorySerializer,  BrandSerializer, ProductSerializer, FirmSerializer

# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    fields = ["id", "name", "category",  "brand",  "stock"] 
    serializer_class = ProductSerializer
