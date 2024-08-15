from rest_framework.viewsets import ModelViewSet
from task_completions.models import TaskCompletion
from .serializers import TaskCompletionSerializer

class TaskCompletionAPIViewSet(ModelViewSet):
    queryset = TaskCompletion.objects.all()
    serializer_class = TaskCompletionSerializer
    