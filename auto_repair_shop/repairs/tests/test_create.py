from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from repairs.factories import AutoFactory


class TestCrateRepairView(TestCase):
    """Тестируем view создания заявки."""

    def test_create_repairs_anonymous(self):
        """Попытка создания формы анонимным пользователем"""

        auto = AutoFactory()
        payload = {
            'description': 'description_test',
            'auto': auto.id
        }

        response = self.client.post(reverse('repairs:create'), data=payload)
        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertIn('/users/login/', response.url)
