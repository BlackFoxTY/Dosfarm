from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.company, name='company'),
    path('company/<slug:slug>/', views.article_detail, name='article_detail'),
]