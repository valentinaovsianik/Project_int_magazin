from django.contrib.auth import login
from django.views.generic import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.contrib.auth.decorators import login_required

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


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        return self.request.user  # Редактирование только своего профиля


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile.html"

    def get_object(self):
        return self.request.user

@login_required
def profile_edit(request):
    user = request.user
    form = UserProfileForm(instance=user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")

    return render(request, "users/profile_edit.html", {"form": form})


