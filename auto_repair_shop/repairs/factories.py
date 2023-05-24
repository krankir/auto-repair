import factory.fuzzy

from repairs.models import Auto, TypeRepair, Works


class TypeRepairFactory(factory.django.DjangoModelFactory):
    """Фабрика тип ремонта."""

    name = factory.Sequence(lambda n: f'test_type_repair{n}')
    hour = factory.fuzzy.FuzzyInteger(5, 12)

    class Meta:
        model = TypeRepair


class WorksFactory(factory.django.DjangoModelFactory):
    """Фабрика места ремонта."""

    name = factory.Sequence(lambda n: f'test_parts_data{n}')
    type_repair = factory.SubFactory(TypeRepairFactory)

    class Meta:
        model = Works


class PlacesFactory(factory.django.DjangoModelFactory):
    """Фабрика места ремонта."""

    name = factory.Sequence(lambda n: f'test_parts_data{n}')

    class Meta:
        model = Auto


class PartsFactory(factory.django.DjangoModelFactory):
    """Фабрика запчастей."""

    name = factory.Sequence(lambda n: f'test_parts_data{n}')

    class Meta:
        model = Auto


class AutoFactory(factory.django.DjangoModelFactory):
    """Фабрика автотранспорта."""

    name = factory.Sequence(lambda n: f'test_name_auto_{n}')

    class Meta:
        model = Auto
