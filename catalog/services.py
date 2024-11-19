from django.core.cache import cache

from catalog.models import Product


def get_products_by_category(category_id):
    """Получение продуктов по категории"""
    return Product.objects.filter(category_id=category_id, is_active=True)


def get_cached_product_list(cache_key="product_list_active", timeout=60 * 15):
    """Возвращает список активных продуктов с кэшированием"""
    products = cache.get(cache_key)
    if products is None:
        # Если данных нет, выполняем запрос к БД
        products = Product.objects.filter(is_active=True)
        cache.set(cache_key, products, timeout)  # Сохраняем данные в кэш
    return products
