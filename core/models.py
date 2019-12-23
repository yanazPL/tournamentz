from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField
    players = models.ManyToManyField(User, related_name = 'played_tournaments')
    hosts = models.ManyToManyField(User, related_name = 'hosted_tournaments')
    max_stages = models.PositiveSmallIntegerField 
    current_stage = models.PositiveSmallIntegerField
    finished = models.BooleanField(default = False)
    category = models.CharField(max_length=200, default="other")
    SINGLE_ELIMINATION = "SE"
    BRACKET_TYPE_CHOICES = [(SINGLE_ELIMINATION, "Single elimination")]
    bracket_type = models.CharField(
        max_length = 2,
        choices = BRACKET_TYPE_CHOICES,
        default = SINGLE_ELIMINATION,
    )
class Match(models.Model):
    player1 = models.ForeignKey(User, null=True, on_delete = models.SET_NULL, related_name="matches_as_p1")
    player2 = models.ForeignKey(User, null=True, on_delete = models.SET_NULL, related_name="matches_as_p2")
    start_time = models.DateTimeField
    finished = models.BooleanField(default=False)
    p1_score = models.PositiveSmallIntegerField
    p2_score = models.PositiveSmallIntegerField
    stage = models.PositiveSmallIntegerField
    tournament = models.ForeignKey(Tournament, on_delete = models.CASCADE, null=True)