from django.shortcuts import render, get_object_or_404
from .models import Vacancy, Resume
from .forms import ResumeForm

# Create your views here.

def career(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'career/career.html', {
        'vacancies': vacancies,
        'breadcrumb_title': 'Карьера',
        'breadcrumb_title_url': '/career/',
    })

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'career/vacancy_detail.html', {
        'vacancy': vacancy,
        'breadcrumb_parent': 'Карьера',
        'breadcrumb_parent_url': '/career/',
        'breadcrumb_title': vacancy.title,
        'breadcrumb_title_url': '',
    })

def resume_submit(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'career/resume_success.html', {
                'breadcrumb_parent': 'Карьера',
                'breadcrumb_parent_url': '/career/',
                'breadcrumb_title': 'Резюме отправлено',
                'breadcrumb_title_url': '',
            })
    else:
        form = ResumeForm(initial={'position': request.GET.get('position', '')})
    return render(request, 'career/resume_form.html', {
        'form': form,
        'breadcrumb_parent': 'Карьера',
        'breadcrumb_parent_url': '/career/',
        'breadcrumb_title': 'Отправить резюме',
        'breadcrumb_title_url': '',
    })

def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'career/vacancies.html', {
        'vacancies': vacancies,
        'breadcrumb_parent': 'Карьера',
        'breadcrumb_parent_url': '/career/',
        'breadcrumb_title': 'Вакансии',
        'breadcrumb_title_url': '/career/vacancies/',
    })