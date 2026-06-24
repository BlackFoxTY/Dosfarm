from django.urls import path
from . import views

urlpatterns = [
    path('career/', views.career, name='career'),
    path('career/vacancy/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('career/resume/', views.resume_submit, name='resume_submit'),
    path('career/vacancies/', views.vacancies, name='vacancies'),
]