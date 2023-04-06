from django.db import models


class Category(models.Model):
    NAME_MAX_LEN = 15
    name = models.CharField(max_length=NAME_MAX_LEN)

    def __str__(self):
        return self.name


class Task(models.Model):
    NAME_MAX_LEN = 30
    DESC_MAX_LEN = 100

    name = models.CharField(max_length=NAME_MAX_LEN)
    description = models.TextField(max_length=DESC_MAX_LEN, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} ({self.category})"
