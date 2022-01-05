from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

GENDERS = (
    ('male', 'Мужской'),
    ('female', 'Женский')
)


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **other_fields):
        if not email:
            raise ValueError('Вы должны ввести eMail')
        if not password:
            raise ValueError('Вы должны ввести пароль')

        user = self.model(
            username=username,
            email=email,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password, **other_fields):
        return self._create_user(username, email, password, **other_fields)

    def create_superuser(self, username, email, password):
        return self._create_user(username, email, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name="Имя пользователя", max_length=256, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=256, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=256)
    creation_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    avatar = models.ImageField(upload_to='images', null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    gender = models.CharField(max_length=256, choices=GENDERS, default='male')

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email.__str__()
