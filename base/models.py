from django.db import models
from user.models import MyUser

class Task(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title