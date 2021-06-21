from rest_framework import  serializers
from .models import RemotePlayerModel

class RemotePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemotePlayerModel
        fields = ('isPlaying', 'currentLink', 'playList')
