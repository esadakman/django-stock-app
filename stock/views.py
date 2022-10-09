from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Brand, Category, Product, Firm, Transaction
from .serializers import CategorySerializer,  BrandSerializer, ProductSerializer, FirmSerializer, TransactionSerializer, CategoryProductsSerializer
# * filtreleme işlemi yapmak için django-filtersı yükledik ve apps'e 'django_filters' ı ekledikten sonra viewsımızda import edip kullanıma hazır hale getirdik
from django_filters.rest_framework import DjangoFilterBackend
# ! admin panelinden oluşturmuş olduğum kullanıcı rolü gruplarını kullanabilmek için DjangoModelPermissions'ı import ediyoruz
from rest_framework.permissions import DjangoModelPermissions

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # ? permissionları kullanabilmek için permission_class'ımı belirtiyorum
    permission_classes = [DjangoModelPermissions]
    # ! filtreleme yaparken iki ayrı filter kullanacağımız için iki filtrs'ımızıda yazıyoruz
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ? ardından ise filterset_fields kısmında filterlamak istediğimiz parametreleri belirtiyoruz
    filterset_fields = ['name']
    search_fields = ['name']

# # ! Category view için 2 tane serializer yazdık ve bunun duruma göre belirlenmesi için get_serializer_class'ı adında yeni bir fonk. yazıyoruz
    def get_serializer_class(self):
        # ? eğer url'imde query params varsa ⬇️ 
        if self.request.query_params.get('name'):
            return CategoryProductsSerializer
        else:
            return super().get_serializer_class()


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]
    # ! filtreleme için aynı işlemleri bu kısımda da yapıyoruz
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    fields = ["id", "name", "category",  "brand",  "stock"]
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name']


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [DjangoModelPermissions]
    # ! filtreleme yaparken iki ayrı filter kullanacağımız için iki filtrs'ımızıda yazıyoruz
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ? ardından ise filterset_fields kısmında filterlamak istediğimiz parametreleri belirtiyoruz
    # ! product'tan sonra ''product__name'' yazarak product'ın name'ine ulaşabilirim
    filterset_fields = ['product', 'firm', 'transaction']
    search_fields = ['firm']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
