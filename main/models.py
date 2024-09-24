import uuid
from django.db import models
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)