from core.models import Tournament, Match, Player
from math import log2, ceil
from random import shuffle
from django.core.exceptions import ObjectDoesNotExist

class EmptyTournamentCreation(TournamentCreation):
    def __init__(self, name, bracket_type):
        self._name = name
        self._bracket_type = bracket_type
    def execute(self):
        Tournament.objects.create(
            name=self._name,
            bracket_type=self._bracket_type,
            players_can_join=True,
        )

class FixedTournamentCreation(TournamentCreation):
    def __init__(self, name, bracket_type, usernames_str):
        self._name = name
        self._bracket_type = bracket_type
        self._player_list = _usernames_to_player_list(usernames_str)

    def execute(self):
        tournament = Tournament.objects.create(
            name = self._name,
            bracket_type = self._bracket_type,
            players_can_join = False
        )
        tournament.add_players(self._player_list)
        MatchesCreation(tournament, self._player_list).execute()

    def _usernames_to_player_list(players_str: str):
        usernames_list = players_str.split()
        player_list = []
        for player_str in usernames_list:
            try:
                # player_list.append(User.objects.get(username=player_str).player)
                player_list.append(Player.objects.get(user__username=player_str))
            except ObjectDoesNotExist:
                # TODO  deisplay error message
                continue
        return player_list

class MatchesCreation:
    def __init__(self, tournament, player_list):
        self._player_list = player_list
        self._avaliable_players = self._player_list
        self._tournament = tournament
        
        #determing tournament size
        self._player_count = len(player_list)
        self._tournament.max_stages = ceil(log2(player_count))
        self._tournament.save()
        self._matches_count = 2 ** (self._tournament.max_stages - 1)



    def execute(self):
        if self._tournament.bracket_type == Tournament.SINGLE_ELIMINATION:
            self.create_se_matches()

    def create_se_matches(self):
        avaliable_players = self._player_list
        shuffle(avaliable_players)
        player_count = len(avaliable_players)
        self._tournament.max_stages = ceil(log2(player_count))
        self._tournament.save()
        matches_count = 2 ** (self._tournament.max_stages - 1)

        # creating first round matches with players
        matches_in_stage = []
        for i in range(matches_count):
            match = Match.objects.create(
                player1=(avaliable_players.pop()
                        if avaliable_players else None),
                player2=None,
                tournament=self._tournament,
                stage=1
                )
            matches_in_stage.append(match)
        for match in matches_in_stage:
            if avaliable_players:
                match.player2 = (avaliable_players.pop()
                                if avaliable_players else None)
            # match.save()
        matches_count //= 2

        # creating other empty matches
        for stage in range(2, self._tournament.max_stages+1):
            for i in range(matches_count):
                match = Match.objects.create(
                    player1=None, player2=None,
                    tournament=self._tournament,
                    stage=stage
                    )
                # match.save()
            matches_count //= 2