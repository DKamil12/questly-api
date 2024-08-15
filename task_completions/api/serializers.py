from rest_framework import serializers
from task_completions.models import TaskCompletion

class TaskCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCompletion
        fields = '__all__'