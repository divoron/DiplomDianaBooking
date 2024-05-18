from django.db import models


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    check_in_date = models.DateField(auto_now_add=True)
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
    deleted = models.DateField(blank=True)

    def __str__(self):
        return (f"User_id: {self.user_id} "
                f"Room_id: {self.room_id}")

# Метод __str__ определен для объектов этой модели, чтобы возвращать строковое представление объекта,
# которым будет : id забронировавшего пользователя и id номера(комнаты).

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

# Класс Meta используется для определения метаданных модели. Здесь устанавливаются человекочитаемые имена для
# единственного и множественного числа (verbose_name и verbose_name_plural соответственно) модели "Booking".
