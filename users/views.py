from rest_framework import generics, status
# ! registerda sadece create işlemi yapacağımız için generics'leri import ediyoruz 
from django.contrib.auth.models import User
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all() # user modelinde kullanacağımız query_set
    serializer_class = RegisterSerializer