# Следующий блок кода определяет сериализатор Django REST Framework для модели Hotel. Сериализаторы используются
# для преобразования объектов Django в JSON и обратно.
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from booking_app.error_messages import NON_UNIQUE_HOTEL_NAME_ERROR, HOTEL_NAME_LEN_ERROR
from booking_app.models.hotel_model import Hotel


# Внутри класса HotelSerializer определен класс Meta, где указывается модель, с которой работает сериализатор,
# а также список полей, которые должны быть сериализованы (в данном случае, используется fields = __all__,
# что означает все поля модели).

# Также определен метод validate_name, который выполняет проверку на уникальность имени отеля (name) и его длину.
# Если имя уже существует в базе данных или его длина не соответствует установленным ограничениям (от 3 до 25
# символов), то генерируется исключение ValidationError с соответствующими сообщениями об ошибках. В противном
# случае, метод возвращает значение имени отеля.


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def validate_name(self, value):
        if Hotel.objects.filter(name=value).exists():
            raise ValidationError(
                NON_UNIQUE_HOTEL_NAME_ERROR
            )

        if len(value) < 3 or len(value) > 25:
            raise ValidationError(
                HOTEL_NAME_LEN_ERROR
            )

        return value
