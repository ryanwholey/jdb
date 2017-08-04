from  rest_framework import serializers
from django.contrib.auth.models import User
from core.models import (
    Player,
    Question,
    Team,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
        )

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
        )

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'username',
            'score',
        )

class TeamPlayersSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'players',
        )

    def setup_eager_loading(self, queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('players')

        return queryset

class PlayerTeamSerializer(serializers.ModelSerializer):

    team = TeamSerializer()

    class Meta:
        model = Player
        fields = (
            'id',
            'username',
            'score',
            'team',
        )

    def setup_eager_loading(self, queryset):
        queryset.select_related('team')

        return queryset

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'answer',
            'value',
            'category',
            'air_date',
            'round',
            'show_number',
        )

