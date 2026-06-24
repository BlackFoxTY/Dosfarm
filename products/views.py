from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product

from django.db.models import Q

def products(request):
    categories = ProductCategory.objects.all()
    return render(request, 'products/products.html', {
        'categories': categories,
        'breadcrumb_title': 'Продукция',
        'breadcrumb_title_url': '/products/',
    })

def category_detail(request, slug):
    category = get_object_or_404(ProductCategory, slug=slug)
    products = category.products.all()
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products,
        'breadcrumb_parent': 'Продукция',
        'breadcrumb_parent_url': '/products/',
        'breadcrumb_title': category.name,
        'breadcrumb_title_url': f'/products/{category.slug}/',
    })

def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(ProductCategory, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug, category=category)
    return render(request, 'products/product_detail.html', {
        'product': product,
        'category': category,
        'breadcrumb_parent': 'Продукция',
        'breadcrumb_parent_url': '/products/',
        'breadcrumb_title': product.name,
        'breadcrumb_title_url': '',
    })

# --
def search(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        words = query.upper().split()  # приводим запрос к верхнему регистру
        q_filter = Q()
        for word in words:
            q_filter |= (
                Q(name__icontains=word) |
                Q(short_description__icontains=word) |
                Q(category__name__icontains=word) |
                Q(application__icontains=word)
            )
        results = Product.objects.filter(q_filter).distinct()
    return render(request, 'products/search.html', {
        'results': results,
        'query': query,
        'breadcrumb_title': f'Поиск: {query}',
        'breadcrumb_title_url': '',
    })