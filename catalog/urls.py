from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (ContactView, HomeView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView,
                    ProductUpdateView, ProductsByCategoryView)

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("category/<int:category_id>/products/", ProductsByCategoryView.as_view(), name="products_by_category"),
]
