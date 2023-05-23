import factory.fuzzy

from repairs.models import Auto


class AutoFactory(factory.django.DjangoModelFactory):
    """Фабрика автотранспорта."""

    name = factory.Sequence(lambda n: f'test_name_auto_{n}')

    class Meta:
        model = Auto

