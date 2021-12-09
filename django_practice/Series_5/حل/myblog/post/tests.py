from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase
from post.api.urls import *
from post.api.serializers import *


class TestPost(APITestCase):

    def setUp(self):
        self.category_attr = {
            'title' : 'category-1',
        }
        self.post_attr = {
            'title' : 'post-1',
            'content' : 'content-1',
        }
        self.post_attr2 = {
            'title' : 'post-2',
            'content' : 'content-2',
        }
        self.post1 = Post.objects.create(**self.post_attr)
        self.post2 = Post.objects.create(**self.post_attr2)
        self.serializer_post = PostSerializer(instance=self.post1)
        self.serializer_post_detail = PostDetailSerializer(instance=self.post2)

        self.category1 = Category.objects.create(**self.category_attr)
        self.serializer_category = CateogrySerializer(instance=self.category1)

    def test_post_list(self):
        data = self.serializer_post.data
        self.assertEqual(set(data.keys()), set(['created_at', 'title']))

    def test_post_detail(self):
        data = self.serializer_post_detail.data
        self.assertEqual(data['title'], str(self.post_attr2['title']))
        self.assertEqual(data['content'], str(self.post_attr2['content']))

    def test_category(self):
        data = self.serializer_category.data
        self.assertEqual(data['title'], str(self.category_attr['title']))
