from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import ContactForm

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:3]
        return context


class ContactView(FormView):
    template_name = 'contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contacts')

    def form_valid(self, form):
        # Получение данных из формы
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
