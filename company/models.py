from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class CompanyArticle(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='company/')
    short_description = models.TextField(help_text='Текст для карточки')
    content = CKEditor5Field(help_text='Полный текст статьи')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Статья компании'
        verbose_name_plural = 'Статьи компании'

    def __str__(self):
        return self.title