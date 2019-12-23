from django.shortcuts import render
from django.views import generic
from core.models import Tournament
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'latest_tournament_list'
    def queryset(self):
        return Tournament.objects.order_by('start_time')[:5]