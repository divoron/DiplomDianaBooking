from django.urls import path
from booking_app.views.hotel_view import HotelListGenericView, RetrieveHotelGenericView
from booking_app.views.room_view import HotelFreeRoomListAPIView

urlpatterns = [path("", HotelListGenericView.as_view()),
               # Маршрут для списка всех отелей. Пустая строка в URL означает, что это базовый URL для списка
               # отелей. Представление HotelListGenericView определено как классовое представление (as_view()
               # используется для преобразования класса во view-функцию)
               path("<int:hotel_id>/", RetrieveHotelGenericView.as_view()),
               # Маршрут для конкретного отеля. <int:hotel_id> означает, что ожидается целое число в URL в
               # качестве идентификатора отеля. Этот идентификатор будет передан в представление для получения,
               # обновления или удаления соответствующего отеля. Представление RetrieveHotelGenericView также
               # определено как классовое представление.
               path("free_rooms/", HotelFreeRoomListAPIView.as_view()),
               ]
