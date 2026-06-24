from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, verbose_name='Название (KZ)')
    name_en = models.CharField(max_length=255, blank=True, verbose_name='Название (EN)')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    PRESCRIPTION_CHOICES = (
        ('rx', 'По рецепту'),
        ('otc', 'Без рецепта'),
    )

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255, blank=True, verbose_name='Название (KZ)')
    name_en = models.CharField(max_length=255, blank=True, verbose_name='Название (EN)')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/')
    short_description = models.TextField()
    short_description_kz = models.TextField(blank=True, verbose_name='Краткое описание (KZ)')
    short_description_en = models.TextField(blank=True, verbose_name='Краткое описание (EN)')
    application = CKEditor5Field(help_text='Показания к применению')
    application_kz = CKEditor5Field(blank=True, verbose_name='Показания (KZ)')
    application_en = CKEditor5Field(blank=True, verbose_name='Показания (EN)')
    prescription = models.CharField(max_length=3, choices=PRESCRIPTION_CHOICES)
    instruction_file = models.FileField(upload_to='instructions/', blank=True, null=True)
    details = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return self.name