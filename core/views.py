from django.shortcuts import render
from products.models import ProductCategory, Product
from press.models import PressArticle
from career.models import Vacancy

def home(request):
    return render(request, 'core/home.html', {
        'products': Product.objects.all()[:6],
        'press_articles': PressArticle.objects.all()[:3],
        'vacancies': Vacancy.objects.all()[:3],
    })

def index(request):
    return render(request, 'core/index.html', {
        'categories': ProductCategory.objects.all()[:6],
        'press_articles': PressArticle.objects.all()[:3],
        'vacancies': Vacancy.objects.all()[:3],
    })