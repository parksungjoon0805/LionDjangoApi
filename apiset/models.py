from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)


class Profile(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()