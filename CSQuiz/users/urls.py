
from django.urls import path, include
from django.views.generic import TemplateView

from .views import Register, EmailConfirm
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/',  Register.as_view(), name='register'),
    path('register/email_confirm/', EmailConfirm.as_view(), name='email_confirm'),
    path('register/email_confirm/fail/', TemplateView.as_view(template_name='registration/email_confirm_fail.html'), name='email_confirm_fail',),
]