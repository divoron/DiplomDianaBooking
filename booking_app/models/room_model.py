from django.db import models
from booking_app.models.hotel_model import Hotel


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey('Hotel',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    room_type = models.CharField(help_text='economy, deluxe, luxury', max_length=8)
    photos = models.ImageField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return (f'Отель: {self.hotel_id}'
                f'Тип номера: {self.room_type} '
                f'Цена за ночь: {self.price_per_night} '
                f'Свободен: {self.available}')
    # Метод __str__ определен для объектов этой модели, чтобы возвращать строковое представление объекта,
    # которым будет тип номера, его цена за ночь и свободен ли он.

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    # Класс Meta используется для определения метаданных модели. Здесь устанавливаются человекочитаемые имена для
    # единственного и множественного числа (verbose_name и verbose_name_plural соответственно) модели "Room".
