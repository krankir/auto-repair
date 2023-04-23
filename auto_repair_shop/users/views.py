from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View

from core.utils import send_email_vor_verify
from users.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class MyLoginView(LoginView):
    """Класс для аутентификации пользователей."""

    form_class = AuthenticationForm


class Register(View):
    """Класс для регистрации пользователей."""

    template_name = 'registration/register.html'

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_vor_verify(request, user)
            return redirect('users:confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class EmailVerify(View):
    """Класс для подтверждения регистрации через email."""

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and default_token_generator.check_token(user,
                                                                    token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError, ValueError, OverflowError, User.DoesNotExist,
                ValidationError):
            user = None
        return user
