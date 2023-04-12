from django.db import models


class Pizza(models.Model):
    SIZE_CHOICES = [
        ('sm', 'Small'),
        ('me', 'Medium'),
        ('la', 'Large'), ]

    name = models.CharField(max_length=30)
    ingredients = models.TextField()
    photo = models.ImageField(upload_to='static/images')
    size = models.CharField(choices=SIZE_CHOICES, max_length=30, default='Medium')

    def __str__(self):
        return f"{self.name}"
