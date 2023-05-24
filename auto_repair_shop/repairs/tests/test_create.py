from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from repairs.factories import AutoFactory
from repairs.models import Repair
from users.factories import UserFactory
from users.models import Role


class TestCrateRepairView(TestCase):
    """Тестируем view создания заявки."""

    def test_create_repair_master(self):
        """Попытка создать заявку мастером."""
        payload = {
            'description': 'description',
            'auto': 1
        }
        master = UserFactory(role=Role.MASTER)
        self.client.force_login(master)
        response = self.client.post(reverse('repairs:create'), data=payload)
        self.assertTrue(response.status_code, HTTPStatus.FOUND)

    def test_create_repair_customer(self):
        """Создание заявки."""
        auto = AutoFactory()
        description = 'description_test'
        payload = {
            'description': description,
            'auto': auto.id
        }
        customer = UserFactory()
        self.client.force_login(customer)

        response = self.client.post(reverse('repairs:create'), data=payload)
        repair = Repair.objects.filter(
            users=customer, description=description
        ).first()
        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(repair)
        self.assertTrue(repair.auto, auto.id)

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
