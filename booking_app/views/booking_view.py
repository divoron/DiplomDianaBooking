from rest_framework.generics import (ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from booking_app.models.booking_model import Booking
from booking_app.serializers.booking_serializer import BookingSerializer
from booking_app.success_messages import (BOOKING_DELETED_MESSAGE,
                                          BOOKING_UPDATED_MESSAGE,
                                          BOOKING_CREATED_MESSAGE)


class BookingListGenericView(ListAPIView):
    # Здесь определяются права доступа, требуемые для доступа к этому представлению.
    # В данном случае, используется IsAuthenticated, что означает,
    # что пользователь должен быть аутентифицирован для доступа к этим операциям.
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = BookingSerializer
    # Это запрос к базе данных для получения всех объектов модели Booking
    queryset = Booking.objects.all()

    # Метод для обработки GET-запросов, которые возвращают список всех бронирований.
    def get(self, request: Request, *args, **kwargs):
        bookings = self.get_queryset()
        if bookings:
            serializer = self.serializer_class(bookings, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

    # Метод для обработки POST - запросов, которые создают новое бронирование на основе данных, предоставленных в
    # запросе.
    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "message": BOOKING_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


# Добавляем класс RetrieveBookingGenericView, который наследуется от RetrieveUpdateDestroyAPIView
# и обеспечивает возможность просмотра, обновления и удаления конкретного бронирования.
class RetrieveBookingGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    # Метод для получения конкретного бронирования по его идентификатору. Он использует get_object_or_404 для получения
    # объекта из базы данных или генерации ошибки 404 Not Found, если объект не найден.
    def get_object(self):
        booking_id = self.kwargs.get("booking_id")
        booking = get_object_or_404(Booking, id=booking_id)
        return booking

    # Метод для обработки GET-запросов на получение конкретного бронирования.
    def get(self, request: Request, *args, **kwargs):
        booking = self.get_object()
        serializer = self.serializer_class(booking)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    # Метод для обработки PUT-запросов на обновление конкретного бронирования. При успешном обновлении бронирования
    # возвращается код состояния 200 OK, а также сообщение об успешном обновлении и обновленные данные бронирования в
    # формате JSON. В случае ошибки валидации возвращается код состояния 400 Bad Request и информация об ошибках в
    # формате JSON.
    def put(self, request: Request, *args, **kwargs):
        booking = self.get_object()
        serializer = self.serializer_class(booking, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": BOOKING_UPDATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    # Метод для обработки DELETE-запросов на удаление конкретного бронирования.
    # При успешном удалении бронирования возвращается код состояния 200 OK и сообщение о успешном удалении.
    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        booking.delete()
        return Response(
            status=status.HTTP_200_OK,
            data=BOOKING_DELETED_MESSAGE
        )
