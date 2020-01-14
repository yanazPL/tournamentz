from django.contrib.auth.models import User
from core.models import Tournament, Match
from math import log2, ceil
from random import shuffle

def tournament_creation(
    tournament,
    name, bracket_type,
    usernames_str):

    tournament.name = name
    tournament.bracket_type = bracket_type
    player_list = usernames_to_player_list(usernames_str)
    if bracket_type == Tournament.SINGLE_ELIMINATION:
        create_se_matches(tournament, player_list)
def usernames_to_player_list(players_str:str):
    usernames_list = players_str.split()
    player_list = []
    for player_str in usernames_list:
        try:
            player_list.append(User.objects.get(username=player_str))
        except:
            #TODO  deisplay error message
            continue
    return player_list


def create_se_matches(tournament, player_list):
    avaliable_players = player_list
    shuffle(avaliable_players)
    player_count = len(player_list)
    tournament.max_stages = ceil(log2(player_count))
    tournament.save()
    matches_count = 2 ** (tournament.max_stages - 1)

    #creating first round matches with players
    matches_in_stage = []
    for i in range(matches_count):
        match = Match(
            player1= (avaliable_players.pop()
                    if avaliable_players else None),
            player2=None,
            tournament=tournament,
            stage=1
            )
        matches_in_stage.append(match)
    for match in matches_in_stage:
        if avaliable_players: 
            match.player2 = (avaliable_players.pop()
                            if avaliable_players else None)
        match.save()
    matches_count //= 2

    #creating other empty matches
    for stage in range(2, tournament.max_stages+1):
        for i in range(matches_count):
            match = Match(
                player1=None, player2=None,
                tournament=tournament,
                stage=stage
                )
            match.save()
        matches_count //= 2

    # for stage in range(1, tournament.max_stages + 1):
    #     matches_in_stage = []
    #     if stage == 1:
    #         for i in range(matches_count):
    #             match = Match(
    #                 player1=avaliable_players.pop(),
    #                 player2=None,
    #                 tournament = tournament
    #                 )
    #             matches_in_stage.append(match)
    #         for match in matches_in_stage:
    #             if avaliable_players: 
    #                 match.player2 = avaliable_players.pop()
    #             match.save()
    #     else:
    #         for i in range(matches_count):
    #             match = Match(
    #                 player1=None, player2=None,
    #                 tournament=tournament,
    #                 stage=stage
    #                 )
    #             match.save()
    #     matches_count //= 2
