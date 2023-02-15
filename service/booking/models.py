from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=55)
    color = models.CharField(max_length=55)
    breed = models.CharField(max_length=55)
    age = models.PositiveIntegerField()
    photo = models.CharField("URL", max_length=512)
    booking = models.BooleanField(default=False)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
