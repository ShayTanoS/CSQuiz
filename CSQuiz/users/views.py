from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from random import randint
from .models import User
from .forms import UserCreationForm, EmailConfirmForm
# Create your views here.
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        request.session['code'] = 100221
        context = {'form': UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data.get('username')
            request.session['password'] = form.cleaned_data.get('password1')
            request.session['email'] = form.cleaned_data.get('email')
            request.session['code'] = randint(100_000, 999_999)
            send_mail(
                'Підтвердження email.',
                f'Your code {request.session["code"]}',
                'cs2quiz2024@gmail.com',
                [request.session['email']]
            )
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
        if form.is_valid():
            if form.cleaned_data['code'] == request.session["code"]:
                user = User.objects.create(username=request.session["username"], email=request.session["email"])
                user.set_password(request.session["password"])
                user.save()
                user = authenticate(username=request.session["username"], password=request.session["password"])
                login(request, user)
                return redirect('home')
        return redirect('email_confirm_fail')


def profile_view(request):
    if request.method == 'GET':
        return render(request, 'profile.html')
