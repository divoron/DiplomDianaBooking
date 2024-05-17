from django.urls import path
from booking_app.views.room_view import RoomsListGenericView, RoomDetailGenericView

urlpatterns = [
    path('', RoomsListGenericView.as_view()),  # Этот маршрут URL привязывает представление RoomsListGenericView к
    # корневому URL-адресу приложения. Таким образом, при обращении к корневому URL будет отображен список номеров.
    path('<int:room_id>/', RoomDetailGenericView.as_view()),  # Этот маршрут URL привязывает представление
    # RoomDetailGenericView к URL-адресу, содержащему идентификатор номера в качестве переменной. Таким образом,
    # при обращении к URL вида /<идентификатор_номера>/ будет отображена информация о конкретном номере.
]
