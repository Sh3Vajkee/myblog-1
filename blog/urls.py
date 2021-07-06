from .models import Article
from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('articles/', views.index, name='articles'),
    path('', views.main_page, name='main_page'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('about/', views.about, name='about'),
    path('search/', views.Search.as_view(), name='search'),
]

