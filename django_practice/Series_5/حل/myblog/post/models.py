from django.db import models
from django.urls import reverse

from django.db.models.signals import pre_save
from myblog.utils import unique_slug_generator

class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, max_length=120, null=True)

    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('category_reverse', kwargs={'slug': self.slug})

    def __str__(self):
        return f"category: {self.title}"


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="post/photos/", blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=120, null=True, blank=True)

    category = models.ManyToManyField(Category)

    class Meta:
        unique_together = ('title', 'slug')

    def __str__(self):
        return f"post: {self.title}"


class Comment(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"comment: {self.title}"


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)