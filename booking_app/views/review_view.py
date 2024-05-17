from rest_framework.generics import (ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from booking_app.models.review_model import Review
from booking_app.serializers.review_serializer import ReviewSerializer
from booking_app.success_messages import REVIEW_CREATED_MESSAGE, REVIEW_UPDATED_MESSAGE, REVIEW_DELETED_MESSAGE


class HotelListGenericView(ListAPIView):
    # Здесь определяются права доступа, требуемые для доступа к этому представлению.
    # В данном случае, используется IsAuthenticated, что означает,
    # что пользователь должен быть аутентифицирован для доступа к этим операциям.
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ReviewSerializer
    # Это запрос к базе данных для получения всех объектов модели Review
    queryset = Review.objects.all()

    # Метод для обработки GET-запросов, которые возвращают список всех отзывов.
    def get(self, request: Request, *args, **kwargs):
        reviews = self.get_queryset()
        if reviews:
            serializer = self.serializer_class(reviews, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

    # Метод для обработки POST - запросов, которые создают новый отзыв на основе данных, предоставленных в запросе.
    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "message": REVIEW_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


# Добавляем класс RetrieveReviewGenericView, который наследуется от RetrieveUpdateDestroyAPIView
# и обеспечивает возможность просмотра, обновления и удаления конкретного отзыва.
class RetrieveReviewGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    # Метод для получения конкретного отзыва по его идентификатору. Он использует get_object_or_404 для получения
    # объекта из базы данных или генерации ошибки 404 Not Found, если объект не найден.
    def get_object(self):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, id=review_id)
        return review

    # Метод для обработки GET-запросов на получение конкретного отзыва.
    def get(self, request: Request, *args, **kwargs):
        review = self.get_object()
        serializer = self.serializer_class(review)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    # Метод для обработки PUT-запросов на обновление конкретного отзыва.
    # При успешном обновлении отзыва возвращается код состояния 200 OK, а также сообщение об успешном обновлении и
    # обновленные данные отзыва в формате JSON. В случае ошибки валидации возвращается код состояния 400 Bad Request и
    # информация об ошибках в формате JSON.
    def put(self, request: Request, *args, **kwargs):
        review = self.get_object()
        serializer = self.serializer_class(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": REVIEW_UPDATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    # Метод для обработки DELETE-запросов на удаление конкретного отзыва.
    # При успешном удалении отзыва возвращается код состояния 200 OK и сообщение о успешном удалении.
    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        review.delete()
        return Response(
            status=status.HTTP_200_OK,
            data=REVIEW_DELETED_MESSAGE
        )



