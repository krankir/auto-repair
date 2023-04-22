from django.urls import path, include

from users.views import Register

app_name = 'users'

urlpatterns = [
    # Подключаем urls.py приложения для работы с пользователями.
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]
