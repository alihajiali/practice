from django.db import models
from django.db.models.deletion import CASCADE

class Product(models.Model):
    STATUS_CHOICES = (
        ("available", "Available"),
        ("unavailable", "Unavailable")
    )
    title = models.CharField(max_length=255, verbose_name="title")
    desc = models.TextField(verbose_name="desc")
    price = models.CharField(max_length=10)
    Comment = models.ForeignKey("Comment", on_delete=models.CASCADE, verbose_name="comment", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category', verbose_name="category")
    tag = models.ManyToManyField('Hashtag', verbose_name="hashtag")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available", verbose_name="status")


    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=250, verbose_name="title")

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    autor = models.OneToOneField("users.User",on_delete=models.CASCADE, verbose_name="writer")
    post = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="post")
    desc = models.TextField(verbose_name="description")
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True, verbose_name="parents")
    title = models.CharField(max_length=255, verbose_name="title")
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title