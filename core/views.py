from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from core.models import Tournament, Match
from django.contrib.auth.models import User
from . import forms
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'latest_tournament_list'
    def queryset(self):
        return Tournament.objects.order_by('start_time')[:5]
class TournamentDetailView(generic.DetailView):
    model = Tournament
    template_name = 'core/tournament_detail.html'
def create_tournament(request):
    if request.method == 'POST':
        form = forms.CreateTournamentForm(request.POST)
        if form.is_valid():
            tournament = Tournament(name=form.cleaned_data['name'])
            tournament.save()
            return HttpResponseRedirect(reverse('tournament_detail', args=(tournament.id,)))
    else:
        form = forms.CreateTournamentForm()

    return render(request, 'core/create_tournament.html', {'form': form})