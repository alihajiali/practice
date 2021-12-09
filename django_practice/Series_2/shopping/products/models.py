from django.db import models
from django.db.models.deletion import CASCADE


class AvailableProductManeger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="available")


class Product(models.Model):
    STATUS_CHOICES = (("available", "Available"), ("unavailable", "Unavailable"))
    title = models.CharField(max_length=255, verbose_name="title")
    desc = models.TextField(verbose_name="desc")
    price = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField("Category", verbose_name="category")
    tag = models.ManyToManyField("Hashtag", verbose_name="hashtag")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available",
        verbose_name="status",
    )
    objects = models.Manager()
    available = AvailableProductManeger()

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=250, verbose_name="title")

    def __str__(self):
        return self.title


class Category(models.Model):
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, verbose_name="parents"
    )
    title = models.CharField(max_length=255, verbose_name="title")
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
