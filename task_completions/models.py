from django.db import models
from users.models import User
from goals.models import Task

# Create your models here.
class TaskCompletion(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    completed_at = models.DateTimeField(auto_now_add=True)
