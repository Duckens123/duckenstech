from django.contrib import admin
from django.urls import path
from dbadmin import views

urlpatterns = [
    path('',views.Dashboard,name='dash'),
    path('addarticle', views.Newarticle,name='newarticle'),
    path('login', views.Login,name='login'),
]