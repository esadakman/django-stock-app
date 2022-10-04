from django.db import models
# ! stock alanında user'a foreign key olarak ekleyeceğim için User'ı import ettim
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(
        Category, related_name="prod_category", on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, related_name="prod_brand", on_delete=models.CASCADE)
    stock = models.SmallIntegerField()


class Stock(models.Model):
    TRANSACTION_TYPE = (
        ("1", "IN"),
        ("2", "OUT"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm,
                                  on_delete=models.CASCADE, related_name="company")
    transaction = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products")
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price_total(self):
        return self.quantity * int(self.price)

    def __str__(self):
        return f'{self.user} - {self.firm} - {self.product}'
