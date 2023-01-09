from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(null=False, blank=False,
                                validators=[validators.MinLengthValidator(2), validate_alphanumeric],
                                max_length=15)
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=True, blank=True, validators=[validators.MinValueValidator(0)])

    def __str__(self):
        return f"ID: {self.pk} | {self.username}"


class Album(models.Model):
    MUSIC_TYPES = ("Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", "Other")

    album_name = models.CharField(null=False, blank=False, max_length=30)
    artist = models.CharField(null=False, blank=False, unique=True, max_length=30)
    genre = models.CharField(null=False, blank=False, max_length=30, choices=[(m, m) for m in MUSIC_TYPES])
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=False, blank=False, verbose_name='Image URL')
    price = models.FloatField(null=False, blank=False, validators=[validators.MinValueValidator(0.0)])

    def __str__(self):
        return f"ID: {self.pk} | {self.album_name}"

    class Meta:
        ordering = ['album_name']
