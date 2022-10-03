from rest_framework import generics, status
# ! registerda sadece create işlemi yapacağımız için generics'leri import ediyoruz 
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all() # user modelinde kullanacağımız query_set
    serializer_class = RegisterSerializer

# ? register işlemi gerçekleştikten sonra dönen dataya token'i eklemek için overwrite işlemi yapmam gerekiyor.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True) # ! if'li is_valid işleminin shortcut'ı
        user = serializer.save() # ? userda'ki create'i user'a atıyoruz
        data = serializer.data

        if Token.objects.filter(user=user).exists():
            # * kullanıcının token'ı mevcutsa 
            token = Token.objects.get(user=user) # ? user'a ilişkin token'ı alıyoruz
            data['token'] = token.key
        else:
            # * kullanıcının token'ı mevcut değilse ⬇️
            data['error'] = 'User dont have token. Please login'
        headers = self.get_success_headers(serializer.data)
        # ! user bilgiletiyle birlikte token bilgisinide göndermek için ⬇️
        # return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message":"User Successfully Created"}, status=status.HTTP_201_CREATED)