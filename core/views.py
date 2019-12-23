from django.shortcuts import render
from django.views import generic
from core.models import Tournament
# Create your views here.
class IndexView(generic.ListView):
    pass