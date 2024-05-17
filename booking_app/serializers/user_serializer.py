from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from booking_app.error_messages import (USERNAME_LEN_ERROR,
                                        USERNAME_NON_UNIQUE_ERROR,
                                        USER_EMAIL_LEN_ERROR,
                                        USER_EMAIL_NON_UNIQUE_ERROR,
                                        USERNAME_REQUIRED_ERROR,
                                        USER_EMAIL_REQUIRED_ERROR)
from booking_app.models.user_model import User
from booking_app.serializers.room_serializer import validate_fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # Это вспомогательная функция для валидации поля. Она проверяет, что поля username и email не является пустыми,
    # уникальны и не превышают максимальную длину.
    def validate_fields(self, value):
        username = value.get('username')
        user_email = value.get('email')

        if not username:
            raise serializers.ValidationError(
                USERNAME_REQUIRED_ERROR
            )
        if len(username) > 25 or len(username) < 2:
            raise serializers.ValidationError(
                USERNAME_LEN_ERROR
            )
        if User.objects.filter(username=value).exists():
            raise ValidationError(
                USERNAME_NON_UNIQUE_ERROR
            )

        if not user_email:
            raise serializers.ValidationError(
                USER_EMAIL_REQUIRED_ERROR
            )
        if len(user_email) > 25 or len(user_email) < 2:
            raise serializers.ValidationError(
                USER_EMAIL_LEN_ERROR
            )
        if User.objects.filter(user_email=value).exists():
            raise ValidationError(
                USER_EMAIL_NON_UNIQUE_ERROR
            )
        return value


# Этот сериализатор используется для представления информации о пользователе, включая его email и бронирования. Он
# также включает метод validate, который вызывает функцию validate_fields для валидации полей перед сохранением.
class UserInfoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    # Вложенный класс, используемый для предоставления дополнительной конфигурации сериализатора.
    class Meta:
        model = User  # Указывает модель, которая будет сериализована.
        fields = [  # Определяет поля модели User, которые должны быть включены в сериализацию. В данном случае
            # включены поля user_id, username, email, bookings.
            'user_id',
            'username',
            'email',
            'bookings',
        ]

    def validate(self, attrs):
        return validate_fields(attrs=attrs)


# Этот сериализатор предназначен для представления всех полей модели пользователя, включая дату создания
# юзера и последнего обновления. Он также включает метод validate, который вызывает ту же функцию validate_fields для
# валидации полей перед сохранением.
class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'username',
            'email',
            'password',
            'bookings',
            'created_at',
            'updated_at',
        ]

    def validate(self, value):
        return validate_fields(value=value)
