from django.db import models


class Cars(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    year = models.IntegerField(default=None)

    # Todo: add a color choice field

    def __str__(self):
        return self.brand
