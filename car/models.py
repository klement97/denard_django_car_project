from django.db import models

from seller.models import Sellers


class Car(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seller = models.ForeignKey(Sellers, related_name="car_list", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.brand
