from django.contrib import admin

from .models import *

@admin.register(UserIdModel)
class UserIdAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(LotoGameModel)
class LotoGameAdmin(admin.ModelAdmin):
    list_display = ['user', 'barrel', 'ticket']
