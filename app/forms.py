from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'pdf_file')
