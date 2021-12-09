from rest_framework import serializers

from post.models import *


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Post
        fields = ['created_at', 'title', 'category']


class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'


class CateogrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
