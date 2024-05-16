from rest_framework.generics import (ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from booking_app.models.hotel_model import Hotel
from booking_app.serializers.hotel_serializer import HotelSerializer
from booking_app.success_messages import HOTEL_CREATED_MESSAGE, HOTEL_UPDATED_MESSAGE, HOTEL_DELETED_MESSAGE


class HotelListGenericView(ListAPIView):
    # Здесь определяются права доступа, требуемые для доступа к этому представлению.
    # В данном случае, используется IsAuthenticated, что означает,
    # что пользователь должен быть аутентифицирован для доступа к этим операциям.
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = HotelSerializer
    # Это запрос к базе данных для получения всех объектов модели Hotel
    queryset = Hotel.objects.all()

    # Метод для обработки GET-запросов, которые возвращают список всех отелей.
    def get(self, request: Request, *args, **kwargs):
        hotels = self.get_queryset()
        if hotels:
            serializer = self.serializer_class(hotels, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

    # Метод для обработки POST - запросов, которые создают новый отель на основе данных, предоставленных в запросе.
    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "message": HOTEL_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


# Добавляем класс RetrieveHotelGenericView, который наследуется от RetrieveUpdateDestroyAPIView
# и обеспечивает возможность просмотра, обновления и удаления конкретного отеля.
class RetrieveHotelGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HotelSerializer

    # Метод для получения конкретного отеля по его идентификатору. Он использует get_object_or_404 для получения
    # объекта из базы данных или генерации ошибки 404 Not Found, если объект не найден.
    def get_object(self):
        hotel_id = self.kwargs.get("hotel_id")
        hotel = get_object_or_404(Hotel, id=hotel_id)
        return hotel

    # Метод для обработки GET-запросов на получение конкретного отеля.
    def get(self, request: Request, *args, **kwargs):
        hotel = self.get_object()
        serializer = self.serializer_class(hotel)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    # Метод для обработки PUT-запросов на обновление конкретного отеля.
    # При успешном обновлении отеля возвращается код состояния 200 OK, а также сообщение об успешном обновлении и
    # обновленные данные отеля в формате JSON. В случае ошибки валидации возвращается код состояния 400 Bad Request и
    # информация об ошибках в формате JSON.
    def put(self, request: Request, *args, **kwargs):
        hotel = self.get_object()
        serializer = self.serializer_class(hotel, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": HOTEL_UPDATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    # Метод для обработки DELETE-запросов на удаление конкретного отеля.
    # При успешном удалении отеля возвращается код состояния 200 OK и сообщение о успешном удалении.
    def delete(self, request, *args, **kwargs):
        hotel = self.get_object()
        hotel.delete()
        return Response(
            status=status.HTTP_200_OK,
            data=HOTEL_DELETED_MESSAGE
        )

