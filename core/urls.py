from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.TournamentDetailView.as_view(), name="tournament_detail"),
    path('create/', views.create_tournament, name="create_tournament"),
]
