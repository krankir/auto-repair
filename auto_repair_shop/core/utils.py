from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


User = get_user_model()


def send_email_vor_verify(request, user):
    """Генерация и отправка email для регистрации."""
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    }
    message = render_to_string(
        'registration/verify_email.html',
        context=context,
    )
    email = EmailMessage(
        'Verify email',
        message,
        to=[user.email],
    )
    email.send()
