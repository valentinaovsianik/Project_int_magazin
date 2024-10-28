from django.urls import path
from catalog.apps import CatalogConfig
from .views import HomeView, ContactView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
