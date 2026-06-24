from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['submitted_at']
        widgets = {
            'position': forms.TextInput(attrs={'placeholder': 'Название позиции'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'ФИО'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Возраст'}),
            'city': forms.TextInput(attrs={'placeholder': 'Город проживания'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7 (___) ___-__-__'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@mail.com'}),
            'desired_salary': forms.TextInput(attrs={'placeholder': 'Например: 200 000 тг'}),
            'work_from1': forms.DateInput(attrs={'type': 'date'}),
            'work_to1': forms.DateInput(attrs={'type': 'date'}),
            'work_from2': forms.DateInput(attrs={'type': 'date'}),
            'work_to2': forms.DateInput(attrs={'type': 'date'}),
            'work_from3': forms.DateInput(attrs={'type': 'date'}),
            'work_to3': forms.DateInput(attrs={'type': 'date'}),
        }