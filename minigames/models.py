from django.db import models

class UserIdModel(models.Model):
    user = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user

class LotoGameModel(models.Model):
    user = models.ForeignKey(UserIdModel, on_delete=models.CASCADE, null=True)
    barrel = models.IntegerField(null=True)
    ticket = models.TextField(max_length=1000, null=True)
