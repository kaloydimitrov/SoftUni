from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    email_address = models.EmailField()
    address = models.TextField(null=True)
    salary = models.IntegerField(null=True)
