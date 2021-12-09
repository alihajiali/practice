from django.db import models
from django.db.models.deletion import CASCADE
# from details.models import Basket

class User(models.Model):
    STATUS_CHOICES = {
        ('s', 'seller'),
        ('c', 'customer'),
    }
    fullname = models.CharField(max_length=254, verbose_name="full name")
    username = models.CharField(max_length=10, unique=True, primary_key = True, verbose_name="user name")
    email = models.EmailField(max_length=254, unique=True, verbose_name="email")
    password = models.CharField(max_length=50, verbose_name="password")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='s', verbose_name="status")
    # basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name="basket", blank=True, null=True)

    def __str__(self):
        return self.username