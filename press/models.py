from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class PressArticle(models.Model):
    title = models.CharField(max_length=255)
    title_kz = models.CharField(max_length=255, blank=True, verbose_name='Заголовок (KZ)')
    title_en = models.CharField(max_length=255, blank=True, verbose_name='Заголовок (EN)')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='press/')
    short_description = models.TextField(help_text='Текст для карточки')
    short_description_kz = models.TextField(blank=True, verbose_name='Краткое описание (KZ)')
    short_description_en = models.TextField(blank=True, verbose_name='Краткое описание (EN)')
    content = CKEditor5Field(help_text='Полный текст статьи')
    content_kz = CKEditor5Field(blank=True, verbose_name='Полный текст (KZ)')
    content_en = CKEditor5Field(blank=True, verbose_name='Полный текст (EN)')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Пресса о нас'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=255)
    title_kz = models.CharField(max_length=255, blank=True, verbose_name='Название (KZ)')
    title_en = models.CharField(max_length=255, blank=True, verbose_name='Название (EN)')
    description = models.TextField(blank=True)
    description_kz = models.TextField(blank=True, verbose_name='Описание (KZ)')
    description_en = models.TextField(blank=True, verbose_name='Описание (EN)')
    image = models.ImageField(upload_to='awards/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Наши награды'
        ordering = ['order']

    def __str__(self):
        return self.title


class PhotoAlbum(models.Model):
    title = models.CharField(max_length=255)
    title_kz = models.CharField(max_length=255, blank=True, verbose_name='Название (KZ)')
    title_en = models.CharField(max_length=255, blank=True, verbose_name='Название (EN)')
    slug = models.SlugField(unique=True)
    cover = models.ImageField(upload_to='albums/covers/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Фототека'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(PhotoAlbum, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='albums/photos/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        ordering = ['order']


class Video(models.Model):
    title = models.CharField(max_length=255)
    title_kz = models.CharField(max_length=255, blank=True, verbose_name='Название (KZ)')
    title_en = models.CharField(max_length=255, blank=True, verbose_name='Название (EN)')
    youtube_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_embed_url(self):
        url = self.youtube_url
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[-1].split('?')[0]
        elif 'watch?v=' in url:
            video_id = url.split('watch?v=')[-1].split('&')[0]
        else:
            video_id = ''
        return f'https://www.youtube.com/embed/{video_id}'

    def get_preview_url(self):
        url = self.youtube_url
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[-1].split('?')[0]
        elif 'watch?v=' in url:
            video_id = url.split('watch?v=')[-1].split('&')[0]
        else:
            video_id = ''
        return f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'