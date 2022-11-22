from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.signUp, name='sign'),
    path('log-in/', views.logIn, name='log'),
    path('home/', views.home, name='home'),
]