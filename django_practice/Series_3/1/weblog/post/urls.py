from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
	path('', views.all_post.as_view(), name='all_post'),
	path('<slug>', views.post_detail.as_view(), name='post_detail'),
	path('category/', views.all_category, name='all_category'),
	path('category/<title>', views.category_detail, name='category_detail'),
]