from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=True, primary_key=True)
