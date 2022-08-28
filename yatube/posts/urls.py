from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),    # Главная страница
    path('group/<slug:slug>/', views.group_posts)   # Список блогов
]