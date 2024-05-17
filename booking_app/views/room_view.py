from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (get_object_or_404,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView, )
from rest_framework import status
from booking_app.models.hotel_model import Hotel
from booking_app.models.room_model import Room
from booking_app.serializers.room_serializer import RoomInfoSerializer, AllRoomsSerializer
from booking_app.success_messages import ROOM_CREATED_MESSAGE, ROOM_UPDATED_MESSAGE, ROOM_DELETED_MESSAGE


class HotelFreeRoomListAPIView(ListAPIView):  # Наследуюсь от ListAPIView потому как мне нужна операция только для
    # чтения списка объектов
    serializer_class = AllRoomsSerializer
    # Здесь определяются права доступа, требуемые для доступа к этому представлению.
    # В данном случае, используется IsAuthenticated, что означает,
    # что пользователь должен быть аутентифицирован для доступа к этим операциям.
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        # Получаем список свободных номеров для каждого отеля
        hotel_rooms = []
        hotels = Hotel.objects.all()
        for hotel in hotels:
            free_rooms = Room.objects.filter(Q(hotel_id=hotel.hotel_id) & Q(available=True))
            hotel_rooms.extend(free_rooms)
        return hotel_rooms


class RoomsListGenericView(ListCreateAPIView):  # Наследуюсь от ListCreateAPIView потому как мне нужна операция не
    # только для чтения, но и для создания объекта

    # Здесь определяются права доступа, требуемые для доступа к этому представлению.
    # В данном случае, используется IsAuthenticated, что означает,
    # что пользователь должен быть аутентифицирован для доступа к этим операциям.
    permission_classes = [
        IsAuthenticated,
    ]
    # Этот атрибут определяет, какой сериализатор будет использоваться для преобразования объектов модели Room в
    # формат JSON и наоборот. В данном случае, используется AllRoomsSerializer, который содержит все поля модели.
    serializer_class = AllRoomsSerializer

    # Этот метод определяет запрос к базе данных для получения списка номеров. Он также выполняет фильтрацию по отелю,
    # если такой фильтр указан в параметрах запроса. Например, если в URL-адресе указан параметр hotel_id,
    # метод фильтрует номера по этому отелю.
    def get_queryset(self):
        queryset = Room.objects.select_related('hotel_id')
        hotel_id = self.request.query_params.get("hotel_id")
        if hotel_id:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset

    # Этот метод обрабатывает GET-запросы на получение списка номеров. Он вызывает метод get_queryset для получения
    # списка номеров и проверяет, существуют ли номера в результате запроса. Если номера найдены, то они сериализуются
    # с помощью AllRoomsSerializer и возвращаются в формате JSON с кодом состояния 200 (OK). Если номера не найдены,
    # возвращается код состояния 204 (No Content).
    def get(self, request: Request, *args, **kwargs):
        filtered_data = self.get_queryset()
        if filtered_data.exists():
            serializer = self.serializer_class(
                instance=filtered_data,
                many=True
            )
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    # Этот метод обрабатывает POST-запросы на создание нового номера. Сначала создается экземпляр сериализатора с
    # данными из запроса. Затем метод is_valid() вызывается для проверки валидности данных. Если данные валидны,
    # новый номер сохраняется в базе данных с помощью метода save() сериализатора. В ответ на успешное создание
    # номера возвращается код состояния 201 (Created) с сообщением об успешном создании и данными новой задачи в
    # формате JSON.
    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "message": ROOM_CREATED_MESSAGE,
                "data": serializer.data
            }
        )


# Добавляем класс RoomDetailGenericView, который является представлением для получения, обновления и удаления
# конкретного номера:
class RoomDetailGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomInfoSerializer

    # Метод для получения конкретного номера по его идентификатору. Идентификатор номера получается из параметров
    # запроса. Если номер с таким идентификатором не найден, возвращается ошибка 404.
    def get_object(self):
        room_id = self.kwargs.get("room_id")
        room = get_object_or_404(Room, id=room_id)
        return room

    # Метод для обработки GET-запросов на получение информации о конкретном номере. Получает номер с помощью метода
    # get_object, сериализует его и возвращает в формате JSON с кодом состояния 200 (OK).
    def get(self, request: Request, *args, **kwargs):
        room = self.get_object()
        serializer = self.serializer_class(room)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    # Метод для обработки PUT-запросов на обновление информации о конкретном номере. Получает номер с помощью метода
    # get_object, затем создает экземпляр сериализатора с данными из запроса и номера. После проверки валидности
    # данных методом is_valid(), происходит обновление номера и возврат успешного ответа с данными обновленного
    # номера в формате JSON и кодом состояния 200 (OK).
    def put(self, request: Request, *args, **kwargs):
        room = self.get_object()
        serializer = self.serializer_class(room, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": ROOM_UPDATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    # Метод для обработки DELETE-запросов на удаление конкретного номера. Получает номер с помощью метода get_object,
    # затем удаляет его из базы данных. В ответ на успешное удаление возвращается сообщение об успешном удалении и код
    # состояния 200 (OK).
    def delete(self, request, *args, **kwargs):
        room = self.get_object()
        room.delete()
        return Response(
            status=status.HTTP_200_OK,
            data=ROOM_DELETED_MESSAGE
        )
