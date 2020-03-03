from django.contrib import admin
from .models import PlayerUser

@admin.register(PlayerUser)
class PlayerUserAdmin(admin.ModelAdmin):
    model = PlayerUser


