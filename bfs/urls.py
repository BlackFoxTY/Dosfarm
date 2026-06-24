from django.urls import path
from . import views

urlpatterns = [
    path('bfs/', views.bfs, name='bfs'),
]