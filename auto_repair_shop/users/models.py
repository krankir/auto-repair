from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Собственная модель пользователя."""

    email = models.EmailField('Электронная почта', max_length=250,  unique=True)
    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь - {self.username}'
