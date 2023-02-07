from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('<int:id>',views.DisplayArticle,name='display_article')
]