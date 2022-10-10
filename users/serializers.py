 # ! user modeli üzerinden bir serializer kullanacağımız için User'ı import ediyoruz
 
from datetime import timezone
from rest_framework import serializers, validators
from django.contrib.auth.models import User  
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

# User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # ? email field'ının bazı default özelliklerini(unique olması ve blank=False olaması) değiştirmek istediğimiz için overwrite etmemiz gerekiyor. 
    # * Bu yüzden validators'ımızı import ediyoruz
    email = serializers.EmailField(
        required=True, 
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    # * Password'larımız içinde bazı özellikleri değiştirmek istiyoruz bu yüzden ⬇
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"} 
        # ! style sayesinde browser API sayfasında ilgili alanın 'password' olarak gözükmesini sağlıyoruz
    )

    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    ) 

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password1', 
        )


# ! öncelikle password ile password 1'in eşleşip eşleşmediğini kontrol ediyoruz
    def validate(self, data):
            if data['password'] != data['password1']:
                raise serializers.ValidationError(
                    {"password": "Password didn't match ... "}
                )
            return data 
    
    def create(self, validated_data):
        # * password'u pop ile alıp daha sonra kullanmak üzere başka bir değişkene atıyoruz,
        password = validated_data.pop("password")
        # ? password1 ise bir daha kullanmıyacağımız için validate_data'nın içinden atıyoruz
        validated_data.pop('password1')
        # ! daha sonra ise user modelinden creation yapıyoruz
        user = User.objects.create(**validated_data)
        # ? set_password ilede userımızın password'unu set ediyoruz
        user.set_password(password)
        # ! son olarak ise yaptığımız işlemleri save ediyoruz
        user.save() 
        # ? register yazma işlemimizi tamamladığımıza göre views.py'a gidip register'ımıza view yazmalıyız 
        return user


# ! User login olduğunda token bilgisinin yanında diğer bilgileride döndürmek için  TokenSerializer'ı overWrite yapmamız gerekiyor 
# ? tokenla birlikte döndüreceğim verileri belirlemek için yeni bir UserSerializer oluşturuyorum
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # * göstermek istediğim verileri seçiyorum
        fields = (
            'username',
            'email'
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        # ? eklemek istediğim field'ları belirtiyorum
        fields = (
            'key',
            'user'
        )       