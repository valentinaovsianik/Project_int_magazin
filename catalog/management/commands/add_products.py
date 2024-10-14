from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product
from django.db import transaction


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                self.stdout.write('Удаление существующих продуктов...')
                Product.objects.all().delete()
                self.stdout.write('Удаление существующих категорий...')
                Category.objects.all().delete()

                self.stdout.write('Создание категорий...')
                # Создание категорий с указанными pk
                Category.objects.create(
                    pk=1,
                    name='Сухие корма',
                    description='Описание категории Сухие корма.'
                )
                Category.objects.create(
                    pk=2,
                    name='Влажные корма',
                    description='Описание категории Влажные корма.'
                )
                Category.objects.create(
                    pk=3,
                    name='Лакомства для собак и кошек',
                    description='Описание категории Лакомства для собак и кошек.'
                )

                self.stdout.write('Загрузка данных из фикстуры...')
                call_command('loaddata', 'product_fixture.json')

            self.stdout.write(self.style.SUCCESS('Успешно загружены данные из фикстуры'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Ошибка при загрузке данных: {e}'))
