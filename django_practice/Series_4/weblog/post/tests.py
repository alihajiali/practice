from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Post, Comment, Category
from model_mommy import mommy

User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        user = mommy.make(User)
        mommy.make(Post, title='test', body='test', writer=user, status='publish', _quantity=10)
        mommy.make(Post, title='test', body='test', writer=user, status='draft', _quantity=5)

    def test_post_list(self):
        url = reverse('postlist')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 10)


class TestComment(APITestCase):
    
    def setUp(self):
        user = mommy.make(User)
        post = mommy.make(Post, title='test', body='test', writer=user, status='publish')
        mommy.make(Comment, title='test', post=post, desc='test', _quantity=10)

    def test_post_list(self):
        url = reverse('categorylist')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 10)