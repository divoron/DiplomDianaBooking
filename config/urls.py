"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', include('booking_app.urls.hotel_url')),  # Маршрут, который добавляет префикс /hotels/ ко
    # всем URL-адресам из приложения booking_app.urls.hotel_url. Функция include() используется для включения
    # URL-адресов из другого модуля, что позволяет организовывать маршруты URL более модульным способом.
    path('rooms/', include('booking_app.urls.room_url')),  # Маршрут, который добавляет префикс /rooms/ ко всем
    # URL-адресам из приложения booking_app.urls.room_url.
    path('users/', include('booking_app.urls.user_url')),  # Маршрут, который добавляет префикс /users/ ко всем
    # URL-адресам из приложения booking_app.urls.user_url.
    path('reviews/', include('booking_app.urls.review_url')),  # Маршрут, который добавляет префикс /reviews/ ко всем
    # URL-адресам из приложения booking_app.urls.review_url.)
    path('bookings/', include('booking_app.urls.booking_url')),  # Маршрут, который добавляет префикс /bookings/ ко всем
    # URL-адресам из приложения booking_app.urls.booking_url.)
]
