from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    edus = Education.objects.all()
    page = Page.objects.all()
    ads = Ads.objects.all()
    anons = Anons.objects.all()

    return render(request, 'index.html', {'edus': edus, 'page': page, 'ads': ads, 'anons': anons})


def edu_detail(request, pk):
    edus = Education.objects.all()
    page = Page.objects.all()
    return render(request, 'edu_detail.html', {'edu': Education.objects.get(id=pk), 'edus': edus, 'page': page})


def page_detail(request, pk):
    edus = Education.objects.all()
    pages = Page.objects.all()
    page = Page.objects.get(id=pk)
    print(page.categories.all())
    return render(request, 'page_detail.html', {'pages': page, 'edu': page.category, 'edus': edus, 'page': pages})






def ads_detail(request, pk):
    ads = Ads.objects.get(id=pk)
    edus = Education.objects.all()
    return render(request, 'ads_detail.html', {'ads': ads, 'edus': edus})

def upload_pdf(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_pdf')
    else:
        form = DocumentForm()
    documents = Document.objects.all()
    return render(request, 'upload_pdf.html', {'form': form, 'documents': documents})

