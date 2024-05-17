from django.contrib import admin
from booking_app.models.hotel_model import Hotel
from booking_app.models.user_model import User

# Класс HotelAdmin определяет пользовательские настройки отображения и взаимодействия с объектами модели Hotel
# в административной панели. list_display указывает, какие поля будут отображаться в списке объектов, list_filter
# добавляет возможность фильтрации по указанным полям, а search_fields позволяет выполнять поиск по указанным полям.


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating',)
    list_filter = ('location', 'rating',)
    search_fields = ('name', 'description',)


# Аналогичные поля и характеристики как в предыдущем классе.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email',)
    list_filter = ('created_at', 'username', 'email',)
    search_fields = ('user_id', 'username', 'email', 'created_at',)
