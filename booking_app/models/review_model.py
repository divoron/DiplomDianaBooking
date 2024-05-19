from django.db import models


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=1000)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return (f'ID отзыва: {self.review_id} '
                f'ID пользователя: {self.user_id} '
                f'ID отеля: {self.hotel_id} '
                f'Комментарий: {self.comment}')
    # Метод __str__ определен для объектов этой модели, чтобы возвращать строковое представление объекта,
    # которым будет ID отзыва, ID пользователя, ID отеля и сам комментарий.

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    # Класс Meta используется для определения метаданных модели. Здесь устанавливаются человекочитаемые имена для
    # единственного и множественного числа (verbose_name и verbose_name_plural соответственно) модели "Review".
