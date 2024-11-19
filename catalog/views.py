from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, TemplateView, UpdateView, View

from catalog.models import Product, Category
from django.contrib import messages

from django.core.cache import cache

from catalog.services import get_products_by_category
from catalog.services import get_cached_product_list

from .forms import ContactForm, ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class HomeView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()[:3]
        return context


class ContactView(FormView):
    template_name = "catalog/contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy("catalog:contacts")

    def form_valid(self, form):
        # Получение данных из формы
        name = form.cleaned_data["name"]
        message = form.cleaned_data["message"]
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"


    # Проверка прав пользователя
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_unpublish"] = self.request.user.has_perm("catalog.can_unpublish_product")
        context["is_moderator"] = self.request.user.groups.filter(name="Moderator Products").exists()
        return context

    def get_queryset(self):
        # Фильтруем только активные продукты
        return get_cached_product_list()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Проверяем принадлежность пользователя к группе
        context["is_moderator"] = self.request.user.groups.filter(name="Moderator Products").exists()
        return context



# Создание продукта
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Привязка владельца
        return super().form_valid(form)


# Редактирование продукта
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        """Проверка, что только владелец или модератор может редактировать продукт."""
        product = super().get_object(queryset)
        if product.owner != self.request.user and not self.request.user.groups.filter(name="Moderator Products").exists():
            raise PermissionDenied("У вас нет прав на редактирование этого продукта.")
        return product

    def form_valid(self, form):
        product = form.instance  # Текущий объект продукта
        is_active = form.cleaned_data.get("is_active")

        # Проверка на отмену публикации
        if not is_active and not self.request.user.has_perm("catalog.can_unpublish_product"):
            form.add_error("is_active", "У вас нет прав для отмены публикации продукта.")
            return self.form_invalid(form)

        messages.success(self.request, "Продукт успешно обновлен.")
        return super().form_valid(form)

    def get_success_url(self):
        # Перенаправление после успешного обновления
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


# Удаление продукта
class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.delete_product"

    def get_object(self, queryset=None):
        """Проверка, что только владелец или модератор могут удалить продукт."""
        product = super().get_object(queryset)
        if product.owner != self.request.user and not self.request.user.groups.filter(
                name="Moderator Products").exists():
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")
        return product


    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("catalog.can_delete_product"):
            return HttpResponseForbidden("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductsByCategoryView(ListView):
    model = Product
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        self.category = get_object_or_404(Category, id=category_id)
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context

