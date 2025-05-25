from django import forms
from .models import studentmodel

class StudentForm(forms.ModelForm):
       class Meta:
        model = studentmodel
        fields = ['name', 'age', 'date_of_birth', 'father_name', 'mother_name', 'address', 'img']  # include img if you have it
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }