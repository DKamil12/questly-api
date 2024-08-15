from rest_framework.viewsets import ModelViewSet
from users.models import Character
from .serializers import CharacterSerializer

class CharacterAPIViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer