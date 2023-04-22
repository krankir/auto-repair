from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class UserCreationForm(UserCreationForm):
    """Кастомная форма регистрации."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)
