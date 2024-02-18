from django.urls import path
from . import views
from .views import UpdatePost

urlpatterns = [
    path('posts/', views.PostList, name='posts'),
    path('create_post/', views.CreatePost, name='create_post'),
    path('update_post/<int:id>/', views.UpdatePost, name='update_post'),
    path('delete_post/<int:id>/', views.DeletePost, name='delete_post'),
]
