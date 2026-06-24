from .models import CompanyArticle
from products.models import ProductCategory

def nav_context(request):
    return {
        'nav_company_articles': CompanyArticle.objects.all()[:8],
        'nav_products': ProductCategory.objects.all()[:8],
        'nav_press_sections': [
            {'title': 'Пресса о нас', 'url': '/press/articles/'},
            {'title': 'Наши награды', 'url': '/press/awards/'},
            {'title': 'Фототека', 'url': '/press/photos/'},
            {'title': 'Видео', 'url': '/press/videos/'},
        ],
    }
