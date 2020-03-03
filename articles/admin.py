from django.contrib import admin
from .models import *

@admin.register(SectionModel)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ThemeModel)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'pablish']

@admin.register(PablicationModel)
class PablicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'create']


