from django.urls import path
from post.api.views import *

app_name = 'post'

urlpatterns = [
    path('post/', api_post, name="post_list"),
    path('post/<slug:slug_text>', api_post_detail, name="post_detail"),
    path('category/', api_category, name="category_list"),
    path('category/<slug:slug_text>', api_category_detail, name="category_detail"),
]