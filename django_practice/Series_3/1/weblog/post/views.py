from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.views import generic

class all_post(generic.ListView):
    template_name = "post/all_post.html"
    context_object_name = 'all_post'
    def get_queryset(self):
        return Post.objects.all().filter(status="publish")
# def all_post(request):
#     all_post = Post.objects.all().filter(status="publish")
#     return render(request, "post/all_post.html", {"all_post": all_post})

class post_detail(generic.DetailView):
    model = Post
    template_name = "post/posts.html"
# def post_detail(request, slug):
#     unique_slug = get_object_or_404(Post, slug = slug)
#     # comment = Post.objects.all().comment_set.desc
#     return render(request, "post/posts.html", {"post": unique_slug})


def all_category(request):
    all_category = Category.objects.all()
    return render(request, "post/all_category.html", {"all_category": all_category})


def category_detail(request, title):
    category = Category.objects.get(title = title)
    all_post = Post.objects.all().filter(category=category)
    return render(request, "post/categorys.html", {"all_post": all_post})