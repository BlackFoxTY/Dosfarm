from django.shortcuts import render, get_object_or_404
from .models import CompanyArticle

def company(request):
    articles = CompanyArticle.objects.all()
    return render(request, 'company/company.html', {
        'articles': articles,
        'breadcrumb_title': 'О компании',
        'breadcrumb_title_url': '/company/',
    })

def article_detail(request, slug):
    article = get_object_or_404(CompanyArticle, slug=slug)
    return render(request, 'company/article_detail.html', {
        'article': article,
        'breadcrumb_parent': 'О компании',
        'breadcrumb_parent_url': '/company/',
        'breadcrumb_title': article.title,
        'breadcrumb_title_url': '',
    })