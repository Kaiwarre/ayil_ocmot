from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'pdf_file')
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'background-color: white',
                'class': 'form-control',
                'placeholder': 'Название файла'}),
            'pdf_file': forms.FileInput(attrs={
                'style': 'background-color: white',
                'class': 'form-control',
                'placeholder': 'Название файла'}),
        }