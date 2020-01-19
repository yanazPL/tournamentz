"""Contains tests for core module."""

from django.test import TestCase
from django.contrib.auth.models import User
from core.services.tournament_creation import (
    tournament_creation, usernames_to_player_list, create_se_matches)
from core.models import Tournament


class UsernamesToPlayersListTest(TestCase):
    """Tests for usernames_to_players_list which converts
    string with usernames to User objects list"""
    def setUp(self):
        for i in range(0, 64):
            User.objects.create(username=("testuser" + str(i + 1)))
        self.test_users = User.objects.filter(username__startswith="testuser")

    def test_one_username(self):
        self.assertListEqual(usernames_to_player_list("testuser1"), [User.objects.get(username="testuser1")])

    def test_no_usernames(self):
        self.assertListEqual(usernames_to_player_list(""), [])

    def test_few_correst_usernames(self):
        usernames = """ testuser1 testuser2 testuser3 testuser4"""
        self.assertListEqual(usernames_to_player_list(usernames), list(self.test_users[:4]))

    def test_all_nonexisting_usernameexpected_results(self):
        usernames = """ xyz 00011234 54342 """
        self.assertListEqual(usernames_to_player_list(usernames), [])

    def test_some_nonexisting_username(self):
        usernames = """testuser1 nonexistinguser testuser2"""
        expected_result = [
            User.objects.get(username="testuser1"),
            User.objects.get(username="testuser2")
            ]
        self.assertListEqual(
            usernames_to_player_list(usernames),
            expected_result
            )


class CreateSeMatchesTest(TestCase):
    def setUp(self):
        self.t = Tournament(name="Test Tournament")
        for i in range(0, 64):
            User.objects.create(username=("testuser" + str(i + 1)))
        self.test_users = User.objects.filter(username__startswith="testuser")

    def test_round_of_2_match_count(self):
        create_se_matches(self.t, [self.test_users[0], self.test_users[1]])
        self.assertEqual(len(self.t.match_set.all()), 1)

    def test_round_of_4_match_count(self):
        create_se_matches(self.t, list(self.test_users[:4]))
        self.assertEqual(len(self.t.match_set.all()), 3)

    def test_round_of_8_match_count(self):
        create_se_matches(self.t, list(self.test_users[:8]))
        self.assertEqual(len(self.t.match_set.all()), 7)

    def test_9_players_stage_1_match_count(self):
        create_se_matches(self.t, list(self.test_users[:9]))
        self.assertEqual(len(self.t.match_set.filter(stage=1)), 8)

    def test_9_payers_all_matches_count(self):
        create_se_matches(self.t, list(self.test_users[:9]))
        self.assertEqual(len(self.t.match_set.all()), 8 + 4 + 2 + 1)
