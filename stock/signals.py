# price_total'ımın otamatik olarak hesaplanması için signals.py oluşturduk 
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Transaction, Product


# ! ilk yapmak istediğimiz şey  transaction modelinde bilgilerin kaydedilmeden önce price'la quantity'nin çarpılıp totalın hesaplanması
# ? Öncelikle receiver'ımızı yazıyoruz ardından parantez içinde yapacağımız işlemi  ve sender'ı belirtiyoruz
@receiver(pre_save, sender=Transaction)
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:
        instance.price_total = instance.quantity * instance.price


# ? ikinci olarak ise post save işleminden sonra quantity'de yapılan işleme göre  product'ın quantity'sini artırmak 
# ? Yine Transaction modelimizi kullanıyoruz ama bu sefer post_save işlemini kullanıcağız
@receiver(post_save, sender=Transaction)
def update_stock(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product_id)
    if instance.transaction == 1:
        # ! instance stoğumuzun değerini kontrol etmek için
        if not product.stock:
            product.stock = instance.quantity
        else:
            product.stock += instance.quantity
    else:
        product.stock -= instance.quantity
    # ? stock değerinin 0'ın altına düşmesi durumunda kullanıcıya error mesajının JSON responseda dönmesini istiyroum, bu yüzden bu işlemi serializers.py'da gerçekleştireceğiz
    product.save()
