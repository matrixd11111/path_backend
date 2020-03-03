from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class PlayerUser(AbstractUser):
    
    health = models.IntegerField(verbose_name='health', default=100, blank=True)
    dexterity = models.IntegerField(verbose_name='dexterity', default=50, blank=True)
    power = models.IntegerField(verbose_name='power', default=20, blank=True)
    endurance = models.IntegerField(verbose_name='endurance', default=50, blank=True)
    cunning = models.IntegerField(verbose_name='cunning', default=20, blank=True)
    deeds = models.IntegerField(verbose_name='deeds', default=1, blank=True)
    evil_good = models.IntegerField(verbose_name='evil_good', default=500, blank=True)
    slug = models.SlugField(max_length=150, unique_for_date='parametrs')
