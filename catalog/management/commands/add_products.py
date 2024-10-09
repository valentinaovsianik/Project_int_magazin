from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        self.stdout.write('Удаление существующих продуктов...')
        Product.objects.all().delete()
        self.stdout.write('Удаление существующих категорий...')
        Category.objects.all().delete()

        # Загружаем данные из фикстуры
        self.stdout.write('Загрузка данных из фикстуры...')
        call_command('loaddata', 'products_fixture.json')
        self.stdout.write(self.style.SUCCESS('Успешно загружены данные из фикстуры'))
