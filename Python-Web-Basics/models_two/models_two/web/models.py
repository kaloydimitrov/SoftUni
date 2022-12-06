from django.db import models


class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    address = models.TextField(null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"
