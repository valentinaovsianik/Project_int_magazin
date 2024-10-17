from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from catalog.views import product_detail, product_list

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),

]
