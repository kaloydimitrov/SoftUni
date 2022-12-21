from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator


def upper(value):
    if not (value[0].isupper()):
        raise ValidationError('Your name must start with a capital letter!')


def alpha(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)]
    )
    first_name = models.CharField(max_length=20, validators=[upper])
    last_name = models.CharField(max_length=20, validators=[upper])
    profile_picture = models.URLField(null=True, blank=True, )


class Plant(models.Model):
    plant_type = models.CharField(max_length=14, choices=(
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants")
    ))
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), alpha])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
