"""Contains tests for core module."""

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from core.services.tournament_creation import (
    tournament_creation, usernames_to_player_list, create_se_matches)
from core.services.tournament_creation2 import(
    TournamentCreation,
    EmptyTournamentCreation,
    FixedTournamentCreation,
    MatchesCreation,
)
from core.models import Tournament, Player


class UsernamesToPlayersListTest(TestCase):
    """Tests for usernames_to_players_list which converts
    string with usernames to User objects list"""
    def setUp(self):
        for i in range(0, 64):
            User.objects.create(username=("testuser" + str(i + 1)))
        self.players = Player.objects.filter(user__username__startswith="testuser")

    def test_one_username(self):
        self.assertListEqual(
            usernames_to_player_list("testuser1"),
            [Player.objects.get(user__username__exact="testuser1")]
        )

    def test_no_usernames(self):
        self.assertListEqual(usernames_to_player_list(""), [])

    def test_few_correct_usernames(self):
        usernames = """ testuser1 testuser2 testuser3 testuser4"""
        self.assertListEqual(usernames_to_player_list(usernames), list(Player.objects.all()[:4]))

    def test_nonexisting_usernames(self):
        usernames = """ xyz 00011234 54342 """
        self.assertRaises(ObjectDoesNotExist)

        
class CreateSeMatchesTest(TestCase):
    def setUp(self):
        self.t = Tournament(name="Test Tournament")
        for i in range(0, 64):
            User.objects.create(username=("testuser" + str(i + 1)))
        self.test_players = Player.objects.filter(user__username__startswith="testuser")

    def test_round_of_2_match_count(self):
        create_se_matches(self.t, [self.test_players[0], self.test_players[1]])
        self.assertEqual(len(self.t.matches.all()), 1)

    def test_round_of_4_match_count(self):
        create_se_matches(self.t, list(self.test_players[:4]))
        self.assertEqual(len(self.t.matches.all()), 3)

    def test_round_of_8_match_count(self):
        create_se_matches(self.t, list(self.test_players[:8]))
        self.assertEqual(len(self.t.matches.all()), 7)

    def test_9_players_stage_1_match_count(self):
        create_se_matches(self.t, list(self.test_players[:9]))
        self.assertEqual(len(self.t.matches.filter(stage=1)), 8)

    def test_9_players_all_matches_count(self):
        create_se_matches(self.t, list(self.test_players[:9]))
        self.assertEqual(len(self.t.matches.all()), 8 + 4 + 2 + 1)

class CreateMatchesTest(TestCase):
    def setUp(self):
        self.t = Tournament(name="Test Tournament", bracket_type=Tournament.SINGLE_ELIMINATION, players_can_join=False)
        for i in range(0, 64):
            User.objects.create(username=("testuser" + str(i + 1)))
        self.test_players = Player.objects.filter(user__username__startswith="testuser")

    def test_round_of_2_match_count(self):
        MatchesCreation(self.t, list(self.test_players)[:2]).execute()
        self.assertEqual(len(self.t.matches.all()), 1)        

    def test_round_of_4_match_count(self):
        MatchesCreation(self.t, list(self.test_players)[:4]).execute()
        self.assertEqual(len(self.t.matches.all()), 3)        

    def test_round_of_8_match_count(self):
        MatchesCreation(self.t, list(self.test_players)[:8]).execute()
        self.assertEqual(len(self.t.matches.all()), 7)        

    def test_9_players_stage_1_match_count(self):
        MatchesCreation(self.t, list(self.test_players[:9])).execute()
        self.assertEqual(len(self.t.matches.filter(stage=1)), 8)

    def test_9_players_all_matches_count(self):
        MatchesCreation(self.t, list(self.test_players[:9])).execute()
        self.assertEqual(len(self.t.matches.all()), 8 + 4 + 2 + 1)
