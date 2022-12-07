from django.db import models

LEVELS = (
        'Trainee',
        'Junior',
        'Middle',
        'Senior'
    )


class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    level = models.IntegerField(choices=((l, LEVELS[l]) for l in range(len(LEVELS))), default='Trainee')
    salary = models.IntegerField()
    works_full_time = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"
