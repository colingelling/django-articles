from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('article/<int:article_id>/', views.article_view, name='article-view'),
    # Add more URL patterns if needed
]
