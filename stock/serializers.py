from pyexpat import model
from rest_framework import serializers
from .models import Category, Brand, Firm, Stock, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name")
class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ("id", "name", "phone", "adress")


class ProductSerializer(serializers.ModelSerializer):
    # * category  ksımında kategorinin ismini görmek için read_only değerlerini=True yapıyoruz
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ("id", "name", "category", "category_id", "brand", "brand_id", "stock")
        # fields = ("id", "name", "category", "brand",  "stock")
