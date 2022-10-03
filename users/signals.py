# # ? kullanıcı register olduğu zaman token alıp login olmasını sağlamak istiyoruz bu yüzden user modelimizde bir user create olduğu zaman tokenda'da bir token oluşturmak için signals.py'ı oluşturduk
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)