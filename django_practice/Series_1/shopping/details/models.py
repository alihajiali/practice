from django.db import models
from django.db.models.deletion import CASCADE
from products.models import Product

class Basket(models.Model):
    STATUS_CHOICESS = (
        ("pey", "Pey"),
        ("later", "Later")
    )
    product = models.ManyToManyField(Product, verbose_name="product")
    status = models.CharField(max_length=20, choices=STATUS_CHOICESS, default="later", verbose_name="status")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} : {self.status}"