from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    name = models.CharField(max_length=30)
    ingredients = models.TextField()
    photo = models.ImageField(upload_to='static/images')
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default=MEDIUM)

    def __str__(self):
        return f"{self.name} ({self.get_size_display()})"


class CartItem(models.Model):
    SIZE_CHOICES = Pizza.SIZE_CHOICES
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='M')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
