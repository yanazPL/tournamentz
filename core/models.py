from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now())
    players = models.ManyToManyField("Player", related_name='played_tournaments', blank=True)
    hosts = models.ManyToManyField("Player", related_name='hosted_tournaments')
    max_stages = models.PositiveSmallIntegerField(default=1)
    current_stage = models.PositiveSmallIntegerField(default=1)
    finished = models.BooleanField(default=False)
    players_can_join = models.BooleanField(default=True)
    category = models.CharField(max_length=200, default="other")
    SINGLE_ELIMINATION = "SE"
    BRACKET_TYPE_CHOICES = [(SINGLE_ELIMINATION, "Single elimination")]
    bracket_type = models.CharField(
        max_length=2,
        choices=BRACKET_TYPE_CHOICES,
        default=SINGLE_ELIMINATION,
    )

    def __str__(self):
        return self.name

    def stages(self):
        return range(1, self.max_stages + 1)

    def matches_of_stage(self, stage):
        return self.tournament.match_set.all().filter(stage=stage)

    def add_players(self, player_list):
        for player in player_list:
            self.players.add(player)
        self.save()

class Match(models.Model):
    player1 = models.ForeignKey("Player", null=True, on_delete=models.SET_NULL, related_name="matches_as_p1")
    player2 = models.ForeignKey("Player", null=True, on_delete=models.SET_NULL, related_name="matches_as_p2")
    start_time = models.DateTimeField(default=timezone.now())
    finished = models.BooleanField(default=False)
    p1_score = models.PositiveSmallIntegerField(default=0)
    p2_score = models.PositiveSmallIntegerField(default=0)
    stage = models.PositiveSmallIntegerField(default=1)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, related_name="matches")

    def winner(self):
        if self.p1_score > self.p2_score:
            return self.player1
        if self.p2_score > self.p1_score:
            return self.player2
        else:
            return None

    def __str__(self):
        return str(self.player1) + " vs " + str(self.player2)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stats = models.OneToOneField("Stats", on_delete=models.CASCADE, null=True)

    @receiver(post_save, sender=User)
    def create_player_profile(sender, instance, created, **kwargs):
        if created:
            Player.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_player_profile(sender, instance, **kwargs):
        instance.player.save()

    def __str__(self):
        return self.user.username


class Stats(models.Model):
    wins = models.PositiveIntegerField(default=0)
    loses = models.PositiveIntegerField(default=0)
    @receiver(post_save, sender=Player)
    def create_player_stats(sender, instance, created, **kwargs):
        if created:
            Stats.objects.create(player=instance)

    @receiver(post_save, sender=Player)
    def save_player_stats(sender, instance, **kwargs):
        instance.stats.save()
