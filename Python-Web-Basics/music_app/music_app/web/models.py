from django.core import validators
from django.db import models


class Profile(models.Model):
    username = models.CharField(null=False, blank=False, validators=[validators.MinLengthValidator(2)], max_length=15)
    email = models.EmailField(null=False, blank=False)
    age = models.ImageField(null=True, blank=True, validators=[validators.MinValueValidator(0)])


class Album(models.Model):
    MUSIC_TYPES = ("Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", "Other")

    album_name = models.CharField(null=False, blank=False, max_length=30),
    artist = models.CharField(null=False, blank=False, unique=True, max_length=30),
    genre = models.CharField(null=False, blank=False, max_length=30, choices=[(m, m) for m in MUSIC_TYPES]),
    description = models.TextField(null=True, blank=True),
    image_url = models.URLField(null=False, blank=False),
    price = models.FloatField(null=False, blank=False, validators=[validators.MinValueValidator(0.0)])
