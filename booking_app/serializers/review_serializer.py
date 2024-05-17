# Следующий блок кода определяет сериализатор Django REST Framework для модели Hotel. Сериализаторы используются
# для преобразования объектов Django в JSON и обратно.
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from booking_app.error_messages import REVIEW_COMM_LEN_ERROR
from booking_app.models.review_model import Review


# Внутри класса ReviewSerializer определен класс Meta, где указывается модель, с которой работает сериализатор,
# а также список полей, которые должны быть сериализованы (в данном случае, используется fields = __all__,
# что означает все поля модели).

# Также определен метод validate_name, который выполняет проверку на длину комментария.
# Если длина комментария не соответствует установленным ограничениям (до 1000
# символов), то генерируется исключение ValidationError с соответствующими сообщениями об ошибках. В противном
# случае, метод возвращает сам комментарий.

def validate_fields(value):
    if len(value) > 1000:
        raise ValidationError(
            REVIEW_COMM_LEN_ERROR
        )
    return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# Этот сериализатор используется для представления информации об отзыве, включая его ID, ID оставившего отзыв
# пользователя, ID отеля, сам комментарий и рейтинг. Он также включает метод validate, который вызывает функцию
# validate_fields для валидации полей перед сохранением.
class ReviewInfoSerializer(serializers.ModelSerializer):
    review = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = [
            'review_id',
            'user_id',
            'hotel_id',
            'comment',
            'rating'
        ]

    def validate(self, attrs):
        return validate_fields(attrs=attrs)


# Этот сериализатор предназначен для представления всех полей отзыва, включая дату создания отзыва и
# последнего обновления. Он также включает метод validate, который вызывает ту же функцию validate_fields для
# валидации полей перед сохранением.
class AllReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'review_id',
            'user_id',
            'hotel_id',
            'comment',
            'rating',
            'created_at',
            'updated_at',
            'deleted_at',
            'deleted'
        ]

    def validate(self, value):
        return validate_fields(value=value)
