from django.urls import path
from . import views

urlpatterns = [
    path('press/', views.press, name='press'),
    path('press/articles/', views.articles, name='press_articles'),
    path('press/articles/<slug:slug>/', views.article_detail, name='press_article_detail'),
    path('press/awards/', views.awards, name='press_awards'),
    path('press/photos/', views.photos, name='press_photos'),
    path('press/photos/<slug:slug>/', views.album_detail, name='album_detail'),
    path('press/videos/', views.videos, name='press_videos'),
]