from django.db import models
from users.models import User

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE

    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    experience_reward = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.title
