from rest_framework import serializers
from booking_app.error_messages import ROOM_TYPE_LENGTH_ERROR, ROOM_TYPE_REQUIRED_ERROR
from booking_app.models.room_model import Room


# Это вспомогательная функция для валидации поля. Она проверяет, что room_type не является пустым и не превышает
# максимальную длину.

def validate_fields(self, attrs):
    room_type = attrs.get('room_type')

    if not room_type:
        raise serializers.ValidationError(
            ROOM_TYPE_REQUIRED_ERROR
        )
    if len(room_type) > 8:
        raise serializers.ValidationError(
            ROOM_TYPE_LENGTH_ERROR
        )
    return attrs


# Этот сериализатор используется для представления информации о номере, включая его отель(ID), тип номера,
# цену за ночь и занятость. Он также включает метод validate, который вызывает функцию validate_fields для валидации
# полей перед сохранением.
class RoomInfoSerializer(serializers.ModelSerializer):
    room = serializers.StringRelatedField()

    class Meta:
        model = Room
        fields = [
            'id',
            'hotel_id',
            'room_type',
            'photos',
            'price_per_night',
            'available'
        ]

    def validate(self, attrs):
        return validate_fields(attrs=attrs)


# Этот сериализатор предназначен для представления всех полей номера, включая дату открытия(создания) номера и
# последнего обновления. Он также включает метод validate, который вызывает ту же функцию validate_fields для
# валидации полей перед сохранением.
class AllRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'hotel_id',
            'room_type',
            'photos',
            'price_per_night',
            'available',
            'created_at',
            'updated_at',
            'deleted_at',
            'deleted'
        ]

    def validate(self, value):
        return validate_fields(value=value)
