from django.shortcuts import render
from .forms import AddPlayerForm, QuizForm
from django.views import View
import requests
from .models import Players
from .functions import url_is_valid, found_info
import random
# Create your views here.
class AddPlayerView(View):
    template_name = 'staff/add_player.html'
    def get(self, request):
        form = AddPlayerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddPlayerForm(request.POST)
        message = 'Wrong'
        if form.is_valid():
            number = form.cleaned_data['number']
            if Players.objects.filter(profile_number=number).exists():
                message = 'Player in DB already exists'
            else:
                if url_is_valid(number):
                    name, surname, nickname, age, country, team, major_winner, major_MVP = found_info(number)
                    Players.objects.create(profile_number=number,
                                           nickname=nickname,
                                           name=name,
                                           surname=surname,
                                           age=age,
                                           country=country,
                                           team=team,
                                           major_winner=major_winner,
                                           major_MVP=major_MVP)
                    message = 'Successfully added ' + nickname + ' to DB'
                else:
                    message = 'Invalid URL'
        form = AddPlayerForm()
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)

class QuizView(View):
    template_name = 'quiz_page.html'
    mystery_player = random.choice(Players.objects.all())
    def get(self, request):
        form = QuizForm()
        context = {'form': form}
        return render(request, self.template_name, context)