from django.contrib import admin
from core.models import (
    Player,
    Team,
    Question,
)

# Register your models here.

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Question)
