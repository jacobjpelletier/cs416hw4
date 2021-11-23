from django.db import models


class Task(models.Model):
    task_item = models.CharField(max_length=25)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_item
