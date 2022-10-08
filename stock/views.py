from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Brand, Category, Product, Firm,Transaction
from .serializers import CategorySerializer,  BrandSerializer, ProductSerializer, FirmSerializer, TransactionSerializer
from django_filters.rest_framework import DjangoFilterBackend 
# * filtreleme işlemi yapmak için django-filtersı yükledik ve apps'e 'django_filters' ı ekledikten sonra viewsımızda import edip kullanıma hazır hale getirdik
# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # ! filtreleme yaparken iki ayrı filter kullanacağımız için iki filtrs'ımızıda yazıyoruz
    filter_backends = [DjangoFilterBackend,filters.SearchFilter] 
    # ? ardından ise filterset_fields kısmında filterlamak istediğimiz parametreleri belirtiyoruz 
    filterset_fields = ['name'] 
    search_fields = ['name']


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # ! filtreleme için aynı işlemleri bu kısımda da yapıyoruz
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]  
    filterset_fields = ['name'] 
    search_fields = ['name']

class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [filters.SearchFilter]  
    search_fields = ['name']

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    fields = ["id", "name", "category",  "brand",  "stock"] 
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]  
    filterset_fields = ['category', 'brand'] 
    search_fields = ['name']

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # ! filtreleme yaparken iki ayrı filter kullanacağımız için iki filtrs'ımızıda yazıyoruz
    filter_backends = [DjangoFilterBackend,filters.SearchFilter] 
    # ? ardından ise filterset_fields kısmında filterlamak istediğimiz parametreleri belirtiyoruz 
    # ! product'tan sonra ''product__name'' yazarak product'ın name'ine ulaşabilirim
    filterset_fields = ['product', 'firm', 'transaction'] 
    search_fields = ['product__name']
