# payments/models.py
from django.db import models

class Order(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
