from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now())
    players = models.ManyToManyField(User, related_name='played_tournaments', blank=True)
    hosts = models.ManyToManyField(User, related_name='hosted_tournaments')
    max_stages = models.PositiveSmallIntegerField(default=1)
    current_stage = models.PositiveSmallIntegerField(default=1)
    finished = models.BooleanField(default=False)
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


class Match(models.Model):
    player1 = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="matches_as_p1")
    player2 = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="matches_as_p2")
    start_time = models.DateTimeField(default=timezone.now())
    finished = models.BooleanField(default=False)
    p1_score = models.PositiveSmallIntegerField(default=0)
    p2_score = models.PositiveSmallIntegerField(default=0)
    stage = models.PositiveSmallIntegerField(default=1)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)

    def winner(self):
        if self.p1_score > self.p2_score:
            return self.player1
        if self.p2_score > self.p1_score:
            return self.player2
        else:
            return None