from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    link = models.URLField()

    def __str__(self):
        return self.title