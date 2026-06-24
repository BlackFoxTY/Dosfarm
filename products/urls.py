from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.category_detail, name='category_detail'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    # path('search/', views.product_search, name='product_search'),
    path('search/', views.search, name='search'),
]