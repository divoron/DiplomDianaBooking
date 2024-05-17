from django.urls import path
from booking_app.views.review_view import ReviewListGenericView, RetrieveReviewGenericView

urlpatterns = [
    path('', ReviewListGenericView.as_view()),  # Этот маршрут URL привязывает представление ReviewListGenericView к
    # корневому URL-адресу приложения. Таким образом, при обращении к корневому URL будет отображен список отзывов.
    path('<int:review_id>/', RetrieveReviewGenericView.as_view()),  # Этот маршрут URL привязывает представление
    # RetrieveReviewGenericView к URL-адресу, содержащему идентификатор отзыва в качестве переменной. Таким образом,
    # при обращении к URL вида /<идентификатор_отзыва>/ будет отображена информация о конкретном отзыве.
]
