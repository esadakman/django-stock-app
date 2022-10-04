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


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ("id", "name", "category", "category_id",
#                   "brand", "brand_id", "stock")
