import jwt
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from HalalBackend import settings
from .models import User
from .serializers import UserSerializer


class RegistrationUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        notUnique = bool(
            User.objects.filter(email=data['email']).first()
            or
            User.objects.filter(username=data['username'])
        )

        if notUnique:
            return Response(data={'message': 'Такой пользователь уже существует'}, status=HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            avatar=data['avatar'],
            phone=data['phone'],
            gender=data['gender']
        )

        return Response(self.get_serializer(user, many=False).data)


class ProfileAPIView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', "").split()[1]
        valid_data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

        user = User.objects.filter(id=valid_data['user_id']).first()

        return Response(data=UserSerializer(user, many=False).data)


class FavoriteAPIView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', "").split()[1]
        valid_data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

        partial = kwargs.pop('partial', False)
        instance = User.objects.get(id=valid_data['user_id'])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(data=serializer.data)