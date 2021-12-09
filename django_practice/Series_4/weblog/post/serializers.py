from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment, Category


class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


User = get_user_model()
class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class post_serializer(serializers.ModelSerializer):
    writer = User_serializer()

    class Meta:
        model = Post
        fields = "__all__"
