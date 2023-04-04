from django.db import models
from django.urls import reverse


class TimeInfo(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )


class Departments(models.Model):
    class Meta:
        verbose_name_plural = 'Departments'

    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Projects(models.Model):
    class Meta:
        verbose_name_plural = 'Projects'

    name = models.CharField(max_length=30),
    deadline = models.DateField()


LEVELS = (
    'Trainee',
    'Junior',
    'Middle',
    'Senior'
)


class Employees(TimeInfo, models.Model):
    class Meta:
        ordering = ['age', 'pk']
        verbose_name_plural = 'Employees'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    level = models.IntegerField(choices=((l, LEVELS[l]) for l in range(len(LEVELS))), default='Trainee')
    salary = models.IntegerField(null=True)
    works_full_time = models.BooleanField(default=True)

    department = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE,  # .SET_NULL  .RESTRICT
        null=True, blank=True,
    )

    project = models.ManyToManyField(
        Projects,
    )

    @property
    def full_name(self):
        return f'{self.first_name} - {self.last_name}'

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.last_name}"
