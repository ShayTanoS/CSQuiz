from django.shortcuts import render
from .forms import AddPlayerForm
from django.views import View
from .models import Players
from .functions import add_player_to_DB, add_team_to_DB, update_player
import random


# Create your views here.
class AddPlayerView(View):
    template_name = 'staff/add_player.html'

    def get(self, request):
        form = AddPlayerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddPlayerForm(request.POST)
        message = []
        if form.is_valid():
            number = form.cleaned_data['number']
            if request.POST['button'] == 'player':
                message.append(add_player_to_DB(number))
            else:
                message = add_team_to_DB(number)
        form = AddPlayerForm()
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)


def update_BD(request):
    players = Players.objects.all()
    context = {'players': players}
    if request.method == 'GET':
        return render(request, 'staff/update_BD.html', context)
    if request.method == 'POST':
        if request.POST['button'] == 'all':
            for player in players:
                update_player(player)
        else:
            current_player = players.filter(full_player_name=request.POST['button']).first()
            update_player(current_player)
        return render(request, 'staff/update_BD.html', context)


class QuizView(View):
    template_name = 'quiz_page.html'

    @classmethod
    def get(cls, request):
        cls.players = Players.objects.all()
        cls.mystery_player = random.choice(cls.players)
        cls.samples_list = []
        context = {'players': cls.players}
        return render(request, cls.template_name, context)

    def post(self, request):
        current_player = self.players.filter(full_player_name=request.POST['button']).first()
        self.samples_list.append(current_player)
        win = current_player ==self.mystery_player
        game_over = win or len(self.samples_list) == 8
        context = {'players': self.players, 'samples_list': self.samples_list,
                   'mystery_player': self.mystery_player, 'win': win, 'game_over': game_over}
        return render(request, self.template_name, context)
