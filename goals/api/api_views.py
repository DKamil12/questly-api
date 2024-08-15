from rest_framework.viewsets import ModelViewSet
from goals.models import Goal, Task
from .serializers import GoalSerializer, TaskSerializer

class GoalAPIViewSet(ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class TaskAPIViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    