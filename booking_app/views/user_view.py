from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (get_object_or_404,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView, )
from rest_framework import status
from booking_app.models.user_model import User
from booking_app.serializers.user_serializer import UserInfoSerializer, AllUsersSerializer
from booking_app.success_messages import USER_CREATED_MESSAGE, USER_UPDATED_MESSAGE, USER_DELETED_MESSAGE


class UsersListGenericView(ListCreateAPIView):
    # Здесь определяются права доступа, требуемые для доступа к этому представлению.
    # В данном случае, используется IsAuthenticated, что означает,
    # что пользователь должен быть аутентифицирован для доступа к этим операциям.
    permission_classes = [
        IsAuthenticated,
    ]
    # Этот атрибут определяет, какой сериализатор будет использоваться для преобразования объектов модели User в
    # формат JSON и наоборот. В данном случае, используется AllRoomsSerializer, который содержит все поля модели.
    serializer_class = AllUsersSerializer

    # Этот метод определяет запрос к базе данных для получения списка пользователей. Он также выполняет фильтрацию по
    # username, если такой фильтр указан в параметрах запроса. Например, если в URL-адресе указан параметр username,
    # метод фильтрует юзеров по этому username.
    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get("username")
        if username:
            queryset = queryset.filter(username=username)
        return queryset

    # Этот метод обрабатывает GET-запросы на получение списка пользователей. Он вызывает метод get_queryset для
    # получения списка пользователей и проверяет, существуют ли пользователи в результате запроса. Если пользователи
    # найдены, то они сериализуются с помощью AllUsersSerializer и возвращаются в формате JSON с кодом состояния 200
    # (OK). Если пользователи не найдены, возвращается код состояния 204 (No Content).
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

    # Этот метод обрабатывает POST-запросы на создание нового пользователя. Сначала создается экземпляр сериализатора
    # с данными из запроса. Затем метод is_valid() вызывается для проверки валидности данных. Если данные валидны,
    # новый пользователь сохраняется в базе данных с помощью метода save() сериализатора. В ответ на успешное
    # создание пользователя возвращается код состояния 201 (Created) с сообщением об успешном создании и данными
    # нового пользователя в формате JSON.
    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "message": USER_CREATED_MESSAGE,
                "data": serializer.data
            }
        )


# Добавляем класс UserDetailGenericView, который является представлением для получения, обновления и удаления
# конкретного пользователя:
class UserDetailGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer

    # Метод для получения конкретного пользователя по его идентификатору. Идентификатор пользователя получается из
    # параметров запроса. Если пользователь с таким идентификатором не найден, возвращается ошибка 404.
    def get_object(self):
        user_id = self.kwargs.get("user_id")
        room = get_object_or_404(User, id=user_id)
        return room

    # Метод для обработки GET-запросов на получение информации о конкретном пользователe. Получает пользователя с
    # помощью метода get_object, сериализует его и возвращает в формате JSON с кодом состояния 200 (OK).
    def get(self, request: Request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    # Метод для обработки PUT-запросов на обновление информации о конкретном пользователe. Получает пользователя с
    # помощью метода get_object, затем создает экземпляр сериализатора с данными из запроса и пользователя. После
    # проверки валидности данных методом is_valid(), происходит обновление пользователe и возврат успешного ответа с
    # данными обновленного пользователe в формате JSON и кодом состояния 200 (OK).
    def put(self, request: Request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": USER_UPDATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    # Метод для обработки DELETE-запросов на удаление конкретного пользователя. Получает пользователя с помощью
    # метода get_object, затем удаляет его из базы данных. В ответ на успешное удаление возвращается сообщение об
    # успешном удалении и код состояния 200 (OK).
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(
            status=status.HTTP_200_OK,
            data=USER_DELETED_MESSAGE
        )
