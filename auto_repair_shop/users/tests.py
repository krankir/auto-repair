from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.forms import UserCreationForm

User = get_user_model()


class TestRegisterView(TestCase):
    """Тестируем view регистрации пользователя."""

    def test_get(self):
        """Получение формы регистрации."""
        response = self.client.get(reverse('users:register'))
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_post_errors_form(self):
        """Тестируем регистрацию с ошибкой."""
        email = 'test_email@yandex.ru'
        data_post = {
            'username': 'username',
            'email': email,
            'password1': '1111',
        }
        response = self.client.post(reverse('users:register'), data=data_post)

        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_post_ok(self):
        """Тестируем что пользователь создался."""
        email = 'test_email@yandex.ru'
        data_post = {
            'username': 'username',
            'email': email,
            'password1': '11qqaazz',
            'password2': '11qqaazz',
        }
        response = self.client.post(reverse('users:register'), data=data_post)

        user = User.objects.get(email=email)

        self.assertEquals(user.email, email)
        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(user.is_authenticated)
