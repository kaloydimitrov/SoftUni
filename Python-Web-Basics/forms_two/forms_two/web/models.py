from django.db import models
from .validators import is_upper, less_than_10, more_than_65


class Person(models.Model):
    first_name = models.CharField(
        max_length=22,
        validators=[is_upper],
        unique=True,
        error_messages={"unique": 'The name is already taken'})
    last_name = models.CharField(
        max_length=22,
        validators=[is_upper])
    age = models.IntegerField(
        validators=[less_than_10, more_than_65],
        default=0)
    profile_image = models.ImageField(
        null=True, blank=True,
        upload_to='images',
        )
    email = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"ID: {self.pk} | {self.first_name} {self.last_name}"
