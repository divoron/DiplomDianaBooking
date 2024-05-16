from django.db import models


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    location = models.CharField(max_length=60)
    description = models.TextField()
    photos = models.ImageField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return (f'Отель: {self.name}/n'
                f'Расположение: {self.location}/n'
                f'Рейтинг: {self.rating}'
                f'Фото: {self.photos}')

    # Метод __str__ определен для объектов этой модели, чтобы возвращать строковое представление объекта,
    # которым будет имя отеля, его расположение, рейтинг и фото.

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

# Класс Meta используется для определения метаданных модели. Здесь устанавливаются человекочитаемые имена для
# единственного и множественного числа (verbose_name и verbose_name_plural соответственно) модели "Hotel".
