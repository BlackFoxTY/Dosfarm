from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Vacancy(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    city = models.CharField('Город', max_length=100)
    requirements = CKEditor5Field('Требования')
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} — {self.city}'


EMPLOYMENT_CHOICES = [
    ('full', 'Полная занятость'),
    ('part', 'Частичная занятость'),
    ('remote', 'Удалённая работа'),
    ('internship', 'Стажировка'),
]

EDUCATION_CHOICES = [
    ('secondary', 'Среднее'),
    ('college', 'Среднее специальное'),
    ('bachelor', 'Бакалавр'),
    ('specialist', 'Специалист'),
    ('master', 'Магистр'),
    ('phd', 'Кандидат наук'),
]


class Resume(models.Model):
    position = models.CharField('Резюме на позицию', max_length=255)

    full_name = models.CharField('ФИО', max_length=255)
    age = models.PositiveIntegerField('Возраст')
    city = models.CharField('Город проживания', max_length=100)
    phone = models.CharField('Телефон', max_length=30)
    email = models.EmailField('Email')

    desired_salary = models.CharField('Желаемая заработная плата', max_length=100, blank=True)
    employment_type = models.CharField('Тип занятости', max_length=20, choices=EMPLOYMENT_CHOICES, blank=True)
    ready_to_relocate = models.BooleanField('Готов к переезду', default=False)
    goal = models.TextField('Цель', blank=True)

    company1 = models.CharField('Компания 1', max_length=255, blank=True)
    position1 = models.CharField('Должность 1', max_length=255, blank=True)
    work_from1 = models.DateField('Период работы с 1', blank=True, null=True)
    work_to1 = models.DateField('Период работы по 1', blank=True, null=True)
    functions1 = models.TextField('Выполняемые функции 1', blank=True)

    company2 = models.CharField('Компания 2', max_length=255, blank=True)
    position2 = models.CharField('Должность 2', max_length=255, blank=True)
    work_from2 = models.DateField('Период работы с 2', blank=True, null=True)
    work_to2 = models.DateField('Период работы по 2', blank=True, null=True)
    functions2 = models.TextField('Выполняемые функции 2', blank=True)

    company3 = models.CharField('Компания 3', max_length=255, blank=True)
    position3 = models.CharField('Должность 3', max_length=255, blank=True)
    work_from3 = models.DateField('Период работы с 3', blank=True, null=True)
    work_to3 = models.DateField('Период работы по 3', blank=True, null=True)
    functions3 = models.TextField('Выполняемые функции 3', blank=True)

    education = models.CharField('Образование', max_length=20, choices=EDUCATION_CHOICES, blank=True)
    languages = models.TextField('Знание языков', blank=True)

    extra_info = models.TextField('Доп. информация', blank=True)
    personal_qualities = models.TextField('Личные качества', blank=True)

    submitted_at = models.DateTimeField('Дата подачи', auto_now_add=True)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.full_name} — {self.position}'