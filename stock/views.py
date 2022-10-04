from django.shortcuts import render
from rest_framework import viewsets
from .models import Brand, Category
from .serializers import CategorySerializer,  BrandSerializer 

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
