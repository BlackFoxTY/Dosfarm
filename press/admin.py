from django.contrib import admin
from .models import PressArticle, Award, PhotoAlbum, Photo, Video

# Register your models here.
@admin.register(PressArticle)
class PressArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3


@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')