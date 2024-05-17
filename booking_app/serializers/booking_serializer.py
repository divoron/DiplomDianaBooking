from rest_framework import serializers
from booking_app.error_messages import BOOKING_OCCUPIED_ERROR
from booking_app.models.booking_model import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, booking):
        # Получаем данные из запроса
        room_id = booking.get('room_id')
        check_in_date = booking.get('check_in_date')
        check_out_date = booking.get('check_out_date')

        # Проверяем, есть ли уже бронирование для данного номера на указанные даты
        existing_bookings = Booking.objects.filter(
            room_id=room_id,
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date,
            deleted_at__isnull=True  # Для активных бронирований
        )

        if existing_bookings.exists():
            raise serializers.ValidationError(
                BOOKING_OCCUPIED_ERROR)

        return booking
