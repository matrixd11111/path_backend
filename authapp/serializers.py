from rest_framework import serializers
from rest_auth.serializers import LoginSerializer

class PlayerLoginSerializers(LoginSerializer):
    
    health = serializers.IntegerField(required=False)
    dexterity = serializers.IntegerField(required=False)
    power = serializers.IntegerField(required=False)
    endurance = serializers.IntegerField(required=False)
    cunning = serializers.IntegerField(required=False)
    deeds = serializers.IntegerField(required=False)
    evil_good = serializers.IntegerField(required=False)
