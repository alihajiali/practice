from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Comment

def all_post(request):
    all_post = Post.objects.all().filter(status="publish")
    return render(request, "post/all_post.html", {"all_post": all_post})

def post_detail(request, slug):
    unique_slug = get_object_or_404(Post, slug = slug)
    # comment = Post.objects.all().comment_set.desc
    return render(request, "post/posts.html", {"post": unique_slug})

def all_category(request):
    all_category = Category.objects.all()
    return render(request, "post/all_category.html", {"all_category": all_category})

def category_detail(request, slug):
    category = Category.objects.get(title = slug)
    all_post = Post.objects.all().filter(category=category)
    return render(request, "post/categorys.html", {"all_post": all_post})







#API
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .serializers import post_serializer, Category_serializer, Comment_serializer

@api_view()
def postlist(request):
    if request.method == "GET":
        all_post = Post.objects.all().filter(status="publish")
        ser_post = post_serializer(all_post, many=True)
        return Response(ser_post.data)


@api_view()
def post(request, id):
    '''way 1'''
    # try :
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     return Response({'ERROR': 'this post does not exist :('})
    # ser_post = post_serializer(post)
    # return Response(ser_post.data)
    '''way 2'''
    post = get_object_or_404(Post, id=id)
    ser_post = post_serializer(post)
    return Response(ser_post.data)


@api_view()
def categorylist(request):
    if request.method == "GET":
        all_category = Category.objects.all()
        ser_category = Category_serializer(all_category, many=True)
        return Response(ser_category.data)


@api_view()
def category(request, id):
    category = get_object_or_404(Category, id=id)
    ser_category = Category_serializer(category)
    return Response(ser_category.data)


@api_view()
def commentlist(request):
    if request.method == "GET":
        all_comment = Comment.objects.all()
        ser_comment = Comment_serializer(all_comment, many=True)
        return Response(ser_comment.data)


@api_view()
def comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    ser_comment = Comment_serializer(comment)
    return Response(ser_comment.data)