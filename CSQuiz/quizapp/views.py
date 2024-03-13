from django.shortcuts import render
from .forms import AddPlayerForm, QuizForm
from django.views import View
from .models import Players
from .functions import add_player_to_DB, add_team_to_DB
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


class QuizView(View):
    template_name = 'quiz_page.html'
    @classmethod
    def get(cls, request):
        form = QuizForm()
        cls.players = Players.objects.all()
        cls.mystery_player = random.choice(cls.players)
        cls.samples_list = []
        print(cls.mystery_player, 'get')
        context = {'form': form, 'players': cls.players}
        return render(request, cls.template_name, context)

    def post(self, request):
        current_player = self.players.filter(full_player_name=request.POST['my_button']).first()
        print(self.mystery_player, 'post')
        self.samples_list.append(current_player)
        form = QuizForm()
        context = {'form': form, 'players': self.players, 'samples_list': self.samples_list,
                   'mystery_player': self.mystery_player}
        return render(request, self.template_name, context)
