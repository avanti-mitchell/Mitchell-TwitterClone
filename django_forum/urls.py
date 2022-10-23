"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
]
"""
"""
from django.urls import path

from . import views

URLPatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]
"""

from django import views
from django.contrib import admin
from django.urls import path, include

from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
]