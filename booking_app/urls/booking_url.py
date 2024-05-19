from django.urls import path
from booking_app.views.booking_view import BookingListGenericView, RetrieveBookingGenericView

urlpatterns = [path("", BookingListGenericView.as_view()),
               # Маршрут для списка всех бронирований. Пустая строка в URL означает, что это базовый URL для списка
               # бронирований. Представление BookingListGenericView определено как классовое представление (as_view()
               # используется для преобразования класса во view-функцию)
               path("<int:booking_id>/", RetrieveBookingGenericView.as_view()),
               # Маршрут для конкретного бронирования. <int:booking_id> означает, что ожидается целое число в URL в
               # качестве идентификатора бронирования. Этот идентификатор будет передан в представление для получения,
               # обновления или удаления соответствующего бронирования. Представление RetrieveBookingGenericView также
               # определено как классовое представление.
               ]
