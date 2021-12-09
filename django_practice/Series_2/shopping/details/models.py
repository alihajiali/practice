from django.db import models
from django.db.models.deletion import CASCADE
from products.models import Product
from users.models import User

class Basket(models.Model):
    STATUS_CHOICESS = (
        ("pey", "Pey"),
        ("later", "Later")
    )
    product = models.ManyToManyField(Product, verbose_name="product")
    status = models.CharField(max_length=20, choices=STATUS_CHOICESS, default="later", verbose_name="status")
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user", blank=True, null=True)

    def __str__(self):
        return f"{self.id} : {self.status}"


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name="basket")
    product = models.ForeignKey(Product, on_delete=CASCADE, null=True)
    number = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"CartItem: {self.product.title}"