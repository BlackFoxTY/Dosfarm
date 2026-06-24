from django.shortcuts import render
from django.core.paginator import Paginator
from .models import PressArticle, Award, PhotoAlbum, Video
from django.shortcuts import render, get_object_or_404

# Create your views here.

def press(request):
    return render(request, 'press/press.html', {
        'breadcrumb_title': 'Пресс-центр',
        'breadcrumb_title_url': '/press/',
    })

def articles(request):
    articles = PressArticle.objects.all()
    return render(request, 'press/articles.html', {
        'articles': articles,
        'breadcrumb_parent': 'Пресс-центр',
        'breadcrumb_parent_url': '/press/',
        'breadcrumb_title': 'Пресса о нас',
        'breadcrumb_title_url': '/press/articles/',
    })

def article_detail(request, slug):
    article = get_object_or_404(PressArticle, slug=slug)
    return render(request, 'press/article_detail.html', {
        'article': article,
        'breadcrumb_parent': 'Пресса о нас',
        'breadcrumb_parent_url': '/press/articles/',
        'breadcrumb_title': article.title,
        'breadcrumb_title_url': '',
    })

def awards(request):
    awards = Award.objects.all()
    return render(request, 'press/awards.html', {
        'awards': awards,
        'breadcrumb_parent': 'Пресс-центр',
        'breadcrumb_parent_url': '/press/',
        'breadcrumb_title': 'Наши награды',
        'breadcrumb_title_url': '/press/awards/',
    })

def photos(request):
    albums = PhotoAlbum.objects.all()
    return render(request, 'press/photos.html', {
        'albums': albums,
        'breadcrumb_parent': 'Пресс-центр',
        'breadcrumb_parent_url': '/press/',
        'breadcrumb_title': 'Фототека',
        'breadcrumb_title_url': '/press/photos/',
    })

def album_detail(request, slug):
    album = get_object_or_404(PhotoAlbum, slug=slug)
    photos = album.photos.all()
    return render(request, 'press/album_detail.html', {
        'album': album,
        'photos': photos,
        'breadcrumb_parent': 'Фототека',
        'breadcrumb_parent_url': '/press/photos/',
        'breadcrumb_title': album.title,
        'breadcrumb_title_url': '',
    })

def videos(request):
    all_videos = Video.objects.all()
    paginator = Paginator(all_videos, 15)
    page = request.GET.get('page')
    videos = paginator.get_page(page)
    return render(request, 'press/videos.html', {
        'videos': videos,
        'breadcrumb_parent': 'Пресс-центр',
        'breadcrumb_parent_url': '/press/',
        'breadcrumb_title': 'Видео',
        'breadcrumb_title_url': '/press/videos/',
    })