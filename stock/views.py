from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Brand, Category, Product, Firm,Stock
from .serializers import CategorySerializer,  BrandSerializer, ProductSerializer, FirmSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend 
# * filtreleme işlemi yapmak için django-filtersı yükledik ve apps'e 'django_filters' ı ekledikten sonra viewsımızda import edip kullanıma hazır hale getirdik
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
    # ! filtreleme yaparken iki ayrı filter kullanacağımız için iki filtrs'ımızıda yazıyoruz
    filter_backends = [DjangoFilterBackend,filters.SearchFilter] 
    # ? ardından ise filterset_fields kısmında filterlamak istediğimiz parametreleri belirtiyoruz 
    # ! product'tan sonra ''product__name'' yazarak product'ın name'ine ulaşabilirim
    filterset_fields = ['product', 'firm', 'transaction'] 