from django.contrib import admin
from .models import Vacancy, Resume

# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'created_at')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'city', 'phone', 'submitted_at')
    readonly_fields = ('submitted_at',)