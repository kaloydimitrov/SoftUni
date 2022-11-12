from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False, primary_key=True)
