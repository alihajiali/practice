from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
	path('', views.all_post, name='all_post'),
	path('<slug>', views.post_detail, name='post_detail'),
	path('category/', views.all_category, name='all_category'),
	path('<slug>', views.category_detail, name='category_detail'),
	path('api/posts/', views.postlist),
	path('api/post/<int:id>/', views.post),
	path('api/categorys/', views.categorylist),
	path('api/category/<int:id>/', views.category),
	path('api/comments/', views.commentlist),
	path('api/comment/<int:id>/', views.comment),
]