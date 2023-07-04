from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


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
    image = models.ImageField(upload_to='static/pictures/pizza/')
    size = models.CharField(max_length=30, choices=SIZE, default=PE)
    price = models.FloatField()

    is_special = models.BooleanField(blank=True, null=True)
    is_offer = models.BooleanField(blank=True, null=True)
    is_vege = models.BooleanField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, default=Pizza.ME)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.pizza}(s) | {self.size}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(upload_to='static/pictures/profile/')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Offers(models.Model):
    image = models.ImageField(upload_to='static/pictures/offers/')
    description = models.TextField()
