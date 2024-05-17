from django.contrib import admin

from booking_app.models.booking_model import Booking
from booking_app.models.hotel_model import Hotel
from booking_app.models.review_model import Review
from booking_app.models.room_model import Room
from booking_app.models.user_model import User

# Класс HotelAdmin определяет пользовательские настройки отображения и взаимодействия с объектами модели Hotel
# в административной панели. list_display указывает, какие поля будут отображаться в списке объектов, list_filter
# добавляет возможность фильтрации по указанным полям, а search_fields позволяет выполнять поиск по указанным полям.


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating',)
    list_filter = ('location', 'rating',)
    search_fields = ('name', 'description',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'photos', 'price_per_night', 'available',)
    list_filter = ('room_type', 'price_per_night', 'available',)
    search_fields = ('room_type', 'price_per_night',)
    # Аналогичные поля и характеристики как в предыдущем классе.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email',)
    list_filter = ('created_at', 'username', 'email',)
    search_fields = ('user_id', 'username', 'email', 'created_at',)
    # Аналогичные поля и характеристики как в предыдущем классе.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user_id', 'room_id', 'check_in_date', 'check_out_date', 'created_at',)
    list_filter = ('user_id', 'room_id', 'check_in_date', 'check_out_date', 'created_at',)
    search_fields = ('user_id', 'room_id', 'check_in_date', 'check_out_date', 'created_at',)
    # Аналогичные поля и характеристики как в предыдущем классе.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'user_id', 'hotel_id', 'comment',)
    list_filter = ('review_id', 'user_id', 'hotel_id',)
    search_fields = ('created_at', 'review_id', 'user_id', 'hotel_id', 'comment',)
    # Аналогичные поля и характеристики как в предыдущем классе.
