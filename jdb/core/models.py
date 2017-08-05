from django.db import models
from django.utils.crypto import get_random_string


class Player(models.Model):
    username = models.CharField(
        unique=True,
        blank=False,
        max_length=255,
    )
    score = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )
    team = models.ForeignKey(
        'Team',
        related_name='players'
    )

    class Meta:
        db_table = 'Players'

    def __str__(self):
        return self.username

class Channel(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey('Team')

    class Meta:
        db_table = 'Channels'

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    token = models.CharField(
        max_length=500,
    )
    secret = models.CharField(
        blank=False,
        max_length=10,
    )

    class Meta:
        db_table = 'Teams'

    def save(self, *args, **kwargs):
        self.secret = get_random_string(10)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    value = models.IntegerField(default=600)
    category = models.CharField(
        max_length=255,
    )
    air_date = models.DateField()
    round = models.CharField(max_length=100)
    show_number = models.CharField(max_length=6)

    class Meta:
        db_table = 'Questions'

    def __str__(self):
        return self.id
