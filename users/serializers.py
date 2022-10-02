from rest_framework import serializers, validators
# ! user modeli üzerinden bir serializer kullanacağımız için User'ı import ediyoruz
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

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
        style={"input_type": "password"} # ! style sayesinde browser API sayfasında ilgili alanın 'password' olarak gözükmesini sağlıyoruz
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
            'is_staff',
            'is_active',
            'is_superuser',
            'date_joined',
            # 'last_login'
        )
