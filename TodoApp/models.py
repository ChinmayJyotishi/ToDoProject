from django.db import models
from django.utils import timezone
# Create your models here.

class todo_model(models.Model):
    task_name=models.CharField(max_length=255)
    task_status=models.BooleanField(default=False)
    time_added = models.DateTimeField(default=timezone.now)

