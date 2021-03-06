from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.TournamentDetailView.as_view(), name="tournament_detail"),
    path('create/', views.create_tournament, name="create_tournament"),
    # path('base/', views.base),
    path('player/<int:id>', views.player_page, name='player_page'),
    path('search/', views.search, name='search'),
]
