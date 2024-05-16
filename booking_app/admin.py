from django.contrib import admin

from booking_app.models.booking_model import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user_id', 'room_id', 'check_in_date', 'check_out_date', 'created_at',)
    list_filter = ('user_id', 'room_id', 'check_in_date', 'check_out_date', 'created_at',)
    search_fields = ('user_id', 'room_id', 'check_in_date', 'check_out_date', 'created_at',)

# Класс BookingAdmin определяет пользовательские настройки отображения и взаимодействия с объектами модели Booking
# в административной панели. list_display указывает, какие поля будут отображаться в списке объектов, list_filter
# добавляет возможность фильтрации по указанным полям, а search_fields позволяет выполнять поиск по указанным полям.
