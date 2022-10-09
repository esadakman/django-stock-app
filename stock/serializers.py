from pyexpat import model
from rest_framework import serializers
from .models import Category, Brand, Firm, Transaction, Product


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
    category_id = serializers.IntegerField(write_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField(write_only=True)
    # stock = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ("id", "name", "category", "category_id",
                  "brand", "brand_id", "stock")
    # ! stock işlemimizin post işleminden sonra update olmasını istiyoruz
    read_only_fields = ('stock',)


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    firm = serializers.StringRelatedField(read_only=True)
    firm_id = serializers.IntegerField(write_only=True, required=False)
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Transaction
        fields = ("id", "user", "firm", "firm_id", "transaction", "product",
                  "product_id", "quantity", "price", "price_total")
        read_only_fields = ('price_total',)

    # ! transaction işleminin geçerliliğini kontrol etmek ve kullanıcıya uyarı mesajı verebilmek için TransactionSerializer içerisinde validate işlemi yapıyoruz
    def validate(self, data):
        # ? data.get diyerek ulaşmak istediğimiz değere ulaşıyoruz
        if data.get('transaction') == 0:
        # ? ardından ulaşmak istediğim product'ı belirtmem gerekiyor ve bunuda id ile belirliyoruz
            product = Product.objects.get(id=data.get('product_id'))
        # ? product'ıda belirledikten sonra quantity'imizin işlem için geçerliliğini kontrol ediyoruz
            if data.get('quantity') > product.stock:
                # ? herhangi bir hata durumunda ise göndereceğimiz hatayı velirtiyoruz
                raise serializers.ValidationError(
                    f'Dont have enough stock. Current stock is {product.stock}'
                )
        # ? son olarakta data'mızı return ediyoruz
        return data

 