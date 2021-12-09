from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from post.models import *
from post.api.serializers import *


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def api_post(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostDetailSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def api_post_detail(request, slug_text):
    try:
        post = Post.objects.get(slug=slug_text)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def api_category(request):
    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CateogrySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def api_category_detail(request, slug_text):
    try:
        category = Category.objects.get(slug=slug_text)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CateogrySerializer(category)
        return Response(serializer.data)

