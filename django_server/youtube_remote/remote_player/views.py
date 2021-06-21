from rest_framework import viewsets
from .serializers import RemotePlayerSerializer
from .models import RemotePlayerModel

class PostViewset(viewsets.ModelViewSet):
    queryset = RemotePlayerModel.objects.all()
    serializer_class = RemotePlayerSerializer
