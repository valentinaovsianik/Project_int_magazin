from django.contrib.auth import login
from django.views.generic import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        user.save()
        login(self.request, user)

        # Отправка приветственного письма
        send_mail(
            subject="Добро пожаловать!",
            message="Спасибо за регистрацию! Добро пожаловать в наш сервис!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return super().form_valid(form)

class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("catalog:product_list")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("catalog:home")