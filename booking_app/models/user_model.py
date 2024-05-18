from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True)
    email = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=50)
    bookings = models.ForeignKey('Booking', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'ID: {self.user_id} '
                f'Username: {self.username} '
                f'Email: {self.email}')

    # Метод __str__ определен для объектов этой модели, чтобы возвращать строковое представление объекта,
    # которым будет его ID, имя и адрес электронной почты.

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

# Класс Meta используется для определения метаданных модели. Здесь устанавливаются человекочитаемые имена для
# единственного и множественного числа (verbose_name и verbose_name_plural соответственно) модели "User".
