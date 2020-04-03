from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from core.models import Tournament, Player
from core.services.tournament_creation import tournament_creation
from . import forms
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'latest_tournament_list'

    def queryset(self):
        return Tournament.objects.order_by('start_time')


class TournamentDetailView(generic.DetailView):
    model = Tournament
    template_name = 'core/tournament_detail.html'


# def base(request):
#     return render(request, 'core/base.html')


def create_tournament(request):
    if request.method == 'POST':
        form = forms.CreateTournamentForm(request.POST)
        if form.is_valid():
            tournament = Tournament(players_can_join=False)
            tournament_creation(
                tournament,
                form.cleaned_data['name'],
                form.cleaned_data['bracket_type'],
                form.cleaned_data['player_list'],
            )
            return HttpResponseRedirect(reverse('tournament_detail', args=(tournament.id,)))
    else:
        form = forms.CreateTournamentForm()

    return render(request, 'core/create_tournament.html', {'form': form})


def player_page(request, id):
    # return HttpResponse(User.objects.get(id=id).username)
    player = get_object_or_404(Player, id=id)
    return render(request, "core/player_page.html", {'player': player})

def search(request):
    if 'q' in request.GET:
        user_input = request.GET['q']
    tournaments = Tournament.objects.filter(name__icontains=user_input)
    players = Player.objects.filter(user__username__icontains=user_input)
    context = {
        'user_input' : user_input,
        'tournaments' : tournaments,
        'players' : players,
    }

    return render(request, 'core/search.html', context)