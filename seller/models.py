from django.db import models


# Create your models here.

class Sellers(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
