from django.db import models

class RemotePlayerModel(models.Model):
    isPlaying = models.BooleanField(default=False)
    currentLink = models.CharField(max_length=200)
    playList = models.TextField()
