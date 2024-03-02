from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from random import randint
from .models import EmailConfirmCodeHelperModel, User
from .form import UserCreationForm, EmailConfirmForm
# Create your views here.
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            code = randint(100_000, 999_999)
            send_mail(
                'Підтвердження email.',
                f'You code {code}',
                'cs2quiz2024@gmail.com',
                [email]
            )
            EmailConfirmCodeHelperModel.objects.create(username=username, code=code, email=email,password=password)
            return redirect('email_confirm')
        context = {'form': form}
        return render(request, self.template_name, context)


class EmailConfirm(View):
    template_name = 'registration/email_confirm.html'
    def get(self, request):
        context = {'form': EmailConfirmForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = EmailConfirmForm(request.POST)
        form_data = EmailConfirmCodeHelperModel.objects.last()
        if form.is_valid():
            if form.cleaned_data['code'] == form_data.code:
                user = User.objects.create(username=form_data.username, email=form_data.email)
                user.set_password(form_data.password)
                user.save()
                user = authenticate(username=form_data.username, password=form_data.password)
                login(request, user)
                form_data.delete()
                return redirect('home')
        form_data.delete()
        return redirect('email_confirm_fail')
