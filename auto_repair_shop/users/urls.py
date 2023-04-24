from django.urls import path, include
from django.views.generic import TemplateView

from .views import Register, EmailVerify, MyLoginView

app_name = 'users'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    # Подключаем urls.py приложения для работы с пользователями.
    path('', include('django.contrib.auth.urls')),
    path('invalid_verify',
         TemplateView.as_view(
             template_name='registration/invalid_verify.html'),
         name='invalid_verify',
         ),
    path('register/', Register.as_view(), name='register'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(),
         name='verify_email',
         ),

    path('confirm_email/',
         TemplateView.as_view(template_name='registration/confirm_email.html'),
         name='confirm_email',
         ),

]
