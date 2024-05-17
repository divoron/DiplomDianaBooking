from django.urls import path
from booking_app.views.user_view import UsersListGenericView, UserDetailGenericView

urlpatterns = [
    path('', UsersListGenericView.as_view()),  # Этот маршрут URL привязывает представление UsersListGenericView к
    # корневому URL-адресу приложения. Таким образом, при обращении к корневому URL будет отображен список
    # пользователей.
    path('<int:user_id>/', UserDetailGenericView.as_view()),  # Этот маршрут URL привязывает представление
    # UserDetailGenericView к URL-адресу, содержащему идентификатор пользователя в качестве переменной. Таким образом,
    # при обращении к URL вида /<идентификатор_пользователя>/ будет отображена информация о конкретном пользователе.
]