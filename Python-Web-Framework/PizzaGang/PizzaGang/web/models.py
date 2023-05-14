from django.db import models
from django.contrib.auth.models import AbstractBaseUser


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
    image = models.ImageField(upload_to='static/pictures/pizza/', blank=True, null=True)
    size = models.CharField(max_length=30, choices=SIZE, blank=True, null=True)
    price = models.FloatField(default=0)

    is_special = models.BooleanField(blank=True, null=True)
    is_offer = models.BooleanField(blank=True, null=True)
    is_vege = models.BooleanField(blank=True, null=True)

    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.pizza}(s) | {self.size}"


class CustomUser(AbstractBaseUser):
    profile_picture = models.ImageField(upload_to='static/pictures/user/profile_pictures/', blank=True, null=True)

    USERNAME_FIELD = 'profile_picture'
