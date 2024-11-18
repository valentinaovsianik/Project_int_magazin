from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Moderator Products")

        # Назначаем разрешения
        can_unpublish_perm = Permission.objects.get(codename="can_unpublish_product")
        delete_product_perm = Permission.objects.get(
            codename="delete_product", content_type__app_label="catalog"
        )

        group.permissions.set([can_unpublish_perm, delete_product_perm])
        group.save()
