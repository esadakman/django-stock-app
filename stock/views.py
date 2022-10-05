from django.shortcuts import render
from rest_framework import viewsets
from .models import Brand, Category, Product, Firm,Stock
from .serializers import CategorySerializer,  BrandSerializer, ProductSerializer, FirmSerializer, StockSerializer

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

class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer