from django.db import models


class Pizza(models.Model):
    PE = "FR"
    SM = "SO"
    ME = "JR"
    LA = "SR"
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
