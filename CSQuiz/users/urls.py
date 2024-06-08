from django.urls import path, include
from django.views.generic import TemplateView
from .views import Register, EmailConfirm, profile_view
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('register/',  Register.as_view(), name='register'),
    path('register/email-confirm/', EmailConfirm.as_view(), name='email_confirm'),
    path('register/email-confirm/fail/', TemplateView.as_view(template_name='registration/email_confirm_fail.html'), name='email_confirm_fail',),
]