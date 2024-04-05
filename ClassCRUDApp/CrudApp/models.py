from django.db import models


class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    assigned_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
