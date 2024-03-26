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


def delete_player(request):
    players = Players.objects.all()
    context = {'players': players}
    if request.method == 'GET':
        return render(request, 'staff/delete_player.html', context)
    if request.method == 'POST':
        current_player = players.filter(full_player_name=request.POST['button']).first()
        current_player.delete()
    return render(request, 'staff/delete_player.html', context)


class QuizView(View):
    template_name = 'quiz_page.html'
    players = Players.objects.all()
    def get(self, request):
        request.session['mystery_player'] = random.choice(self.players).profile_number
        request.session['samples_list'] = []
        context = {'players': self.players}
        return render(request, self.template_name, context)

    def post(self, request):
        mystery_player = self.players.get(profile_number=request.session['mystery_player'])
        current_player = self.players.get(full_player_name=request.POST['button'])
        samples_list = [self.players.get(profile_number=i) for i in request.session['samples_list']]
        win = current_player == mystery_player
        game_over = win or len(samples_list)+1 >= 8
        if game_over:
            user = request.user
            if user.is_authenticated:
                samples_list.append(current_player)
                if win:
                    user.quizzes_win += 1
                else:
                    user.quizzes_lose += 1
                user.save()
        else:
            request.session['samples_list'].append(current_player.profile_number)
            request.session.modified = True
            samples_list.append(current_player)
        context = {'players': self.players, 'samples_list': samples_list,
                   'mystery_player': mystery_player, 'win': win, 'game_over': game_over}
        return render(request, self.template_name, context)
