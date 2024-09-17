import uuid
from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()