from django.urls import path
from blog.apps import BlogConfig
from .views import BlogPostCreateView, BlogPostDetailView, BlogPostListView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('new/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),

]