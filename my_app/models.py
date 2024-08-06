from django.db import models

# Create your models here.

class games(models.Model):
    age_category = (
        ('child', 'child'),
        ('adult', 'adult'),
        ('aged person', 'aged person')
    )
    ride_name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    timings = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=age_category)



