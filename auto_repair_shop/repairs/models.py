from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Status(models.TextChoices):
    """Статус заявок на ремонт."""

    CREATED = 'CREATED', 'Новая заявка от клиента'
    CONFIRMED = 'CONFIRMED', 'Подтверждена техником'
    READY_TO_WORK = 'READY_TO_WORK', 'Готова к работе'
    PROGRESS = 'PROGRESS', 'В работе'
    VERIFICATION = 'VERIFICATION', 'Ремонт выполнен'
    TESTS = 'TESTS', 'На тестирование'
    RE_REPAIR = 'RE_REPAIR', 'На доработку'

    @classmethod
    def statuses_for_list_master(cls):
        """Заявки, которые видит техник."""
        return [
            cls.CONFIRMED, cls.TESTS
        ]

    @classmethod
    def statuses_for_list_technician(cls):
        """Заявки, которые видит техник."""
        return [
            cls.CREATED, cls.VERIFICATION
        ]

    @classmethod
    def statuses_for_list_worker(cls):
        """Заявки, которые видит мастер."""
        return [
            cls.READY_TO_WORK, cls.PROGRESS, cls.RE_REPAIR
        ]


class Repair(models.Model):
    """Заявка на ремонт."""

    users = models.ManyToManyField(
        User, related_name='repairs', verbose_name='Участники заявки',
    )
    description = models.TextField(verbose_name='Описание поломки')
    status = models.CharField(
        max_length=50,
        choices=Status.choices,
        verbose_name='Статус заявки',
        default=Status.CREATED,
    )
    time_to_work = models.DateTimeField(
        verbose_name='Время начала работы', null=True, blank=True,
    )
    places_to_work = models.ForeignKey(
        'PlacesToWork',
        related_name='place_repairs',
        on_delete=models.PROTECT,
        verbose_name='место для ремонта',
        null=True,
        blank=True,
    )
    auto = models.ForeignKey(
        'Auto',
        related_name='auto_repairs',
        on_delete=models.PROTECT,
        verbose_name='Автомобиль',
        null=True,
        blank=True,
    )
    type_repair = models.ForeignKey(
        'TypeRepair',
        related_name='type_repairs',
        on_delete=models.PROTECT,
        verbose_name='Тип ремонта',
        null=True,
        blank=True,
    )
    works = models.ManyToManyField(
        'Works',
        verbose_name='Работы',
        related_name='work_repairs',
    )
    parts = models.ManyToManyField(
        'Parts',
        verbose_name='Запчасти',
        related_name='part_repairs',
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Статус заявки {self.pk} :{self.status}'

    def get_absolute_url(self):
        return reverse('repairs:detail', kwargs={'pk': self.pk})


class PlacesToWork(models.Model):
    """Место ремонта."""

    name = models.CharField(max_length=100, verbose_name='место ремонта')

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'Места работ'

    def __str__(self):
        return f'Ремонтируется в :{self.name}'


class Auto(models.Model):
    """Класс наименования авто"""

    name = models.CharField(max_length=50, verbose_name='марка авто')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'Автомобиль :{self.name}'


class TypeRepair(models.Model):
    """Тип Ремонта."""

    name = models.CharField(max_length=200, verbose_name='Тип ремонта')
    duration_of_work = models.PositiveSmallIntegerField(
        verbose_name='продолжительность ремонта',
    )

    class Meta:
        verbose_name = 'Тип ремонта'
        verbose_name_plural = 'Типы ремонтов'

    def __str__(self):
        return f'Ремонт :{self.name}'


class Parts(models.Model):
    """Класс наименования запчастей."""

    name = models.CharField(max_length=50, verbose_name='Запчасть')

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'

    def __str__(self):
        return f'Запчасть :{self.name}'


class Works(models.Model):
    """Класс наименования работы."""

    name = models.CharField(max_length=50, verbose_name='Работа')
    type_repair = models.ForeignKey(
        'TypeRepair',
        related_name='works',
        verbose_name='Тип работы',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return f'Работа :{self.name}'
