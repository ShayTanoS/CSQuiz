from django.shortcuts import render
from .forms import AddPlayerForm, QuizForm
from django.views import View
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
                    name, surname, nickname, age, country, team, major_winner, major_MVP, full_player_name = found_info(
                        number)
                    Players.objects.create(profile_number=number,
                                           nickname=nickname,
                                           name=name,
                                           surname=surname,
                                           age=age,
                                           country=country,
                                           team=team,
                                           major_winner=major_winner,
                                           major_MVP=major_MVP,
                                           full_player_name=full_player_name)
                    message = 'Successfully added ' + nickname + ' to DB'
                else:
                    message = 'Invalid URL'
        form = AddPlayerForm()
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)


class QuizView(View):
    template_name = 'quiz_page.html'
    samples_list = []
    players = Players.objects.all()

    def get(self, request):
        form = QuizForm()
        self.samples_list.clear()
        self.mystery_player = random.choice(self.players)
        context = {'form': form, 'players': self.players}
        return render(request, self.template_name, context)

    def post(self, request):
        current_player = self.players.filter(full_player_name=request.POST['my_button']).first()
        self.samples_list.append(current_player)
        form = QuizForm()
        context = {'form': form, 'players': self.players, 'samples_list': self.samples_list}
        return render(request, self.template_name, context)
