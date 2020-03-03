from rest_framework import serializers

from .models import *

class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIdModel
        fields = ['user']

class LotoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotoGameModel
        fields = ['user', 'barrel', 'ticket']
