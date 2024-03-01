
from django.urls import path, include
from .views import Register, EmailConfirm
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/',  Register.as_view(), name='register'),
    path('register/email_confirm/', EmailConfirm.as_view(), name='email_confirm')
]