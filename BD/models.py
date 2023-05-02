from django.db import models


# Create your models here.

class Product(models.Model):
    linkWeb = models.TextField()
    link = models.TextField()
    desc = models.TextField()
    price = models.CharField(max_length = 200)

