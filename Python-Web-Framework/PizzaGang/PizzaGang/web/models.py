from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cart =


class Pizza(models.Model):
    PE = "PE"
    SM = "SM"
    ME = "ME"
    LA = "LA"
    SIZE = [
        (PE, "Personal"),
        (SM, "Small"),
        (ME, "Medium"),
        (LA, "Large"),
    ]

    name = models.CharField(max_length=30)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='static/pictures/', blank=True, null=True)
    size = models.CharField(max_length=30, choices=SIZE, blank=True, null=True)
    is_offer = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class RealCart(models.Model):
    real_cart = models.ForeignKey(RealCart, on_delete=models.CASCADE)


class Cart(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

