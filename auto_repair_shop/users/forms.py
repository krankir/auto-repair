from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm,
    AuthenticationForm as DjangoAuthenticationForm,
)
from django.core.exceptions import ValidationError

from core.utils import send_email_vor_verify

User = get_user_model()


class AuthenticationForm(DjangoAuthenticationForm):
    """Кастомная модель Аутентификации пользователя."""

    def clean(self):
        super().clean()
        if not self.user_cache.email_verify:
            send_email_vor_verify(self.request, self.user_cache)
            raise ValidationError(
                'Email not verify? check your email',
                code='invalid_login',
            )


class UserCreationForm(DjangoUserCreationForm):
    """Кастомная форма регистрации пользователя."""

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ("username", "email",)
