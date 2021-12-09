from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    STATUS = (
        ("publish", "انتشار"),
        ("draft", "پیش نویس")
    )
    title = models.CharField(max_length=200, verbose_name="عنوان", null=True, blank=True)
    slug = models.SlugField(verbose_name="آدرس", allow_unicode=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده", null=True, blank=True)
    # body = models.TextField(verbose_name="متن")
    body = RichTextUploadingField(verbose_name="متن", null=True, blank=True)
    image = models.ImageField(upload_to='uploads',null=True,blank=True)
    like = models.IntegerField(default=0, null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    publish_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default="draft", verbose_name="حالت انتشار")
    tag = models.ManyToManyField('Tag', null=True, blank=True)
    category = models.ManyToManyField('Category', null=True, blank=True)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('title category' ,max_length=255, null=True, blank=True)
    desc = RichTextUploadingField(null=True, blank=True)   
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField('title category' ,max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('عنوان' ,max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title