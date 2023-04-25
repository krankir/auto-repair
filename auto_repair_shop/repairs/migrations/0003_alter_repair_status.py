# Generated by Django 3.2.16 on 2023-04-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_works_type_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Новая заявка от клиента'), ('CONFIRMED', 'Подтверждена техником'), ('READY_TO_WORK', 'Готова к работе'), ('PROGRESS', 'В работе'), ('VERIFICATION', 'Ремонт выполнен'), ('TESTS', 'На тестирование'), ('RE_REPAIR', 'На доработку')], default='CREATED', max_length=50, verbose_name='Статус заявки'),
        ),
    ]