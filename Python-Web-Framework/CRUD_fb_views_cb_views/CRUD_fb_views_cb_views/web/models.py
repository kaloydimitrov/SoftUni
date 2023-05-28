from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
