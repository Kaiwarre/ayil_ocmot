from django.shortcuts import render
from .models import *


def home(request):
    edus = Education.objects.all()
    page = Page.objects.all()
    ads = Ads.objects.all()
    anons = Anons.objects.all()
    footers = Footer.objects.all()
    images = EduImages.objects.exclude(edu__isnull=False)
    socsetis = SocSeti.objects.all()

    return render(request, 'index.html', {'edus': edus, 'page': page, 'ads': ads, 'anons': anons, 'images': images, 'footers': footers, 'socsetis': socsetis})


def edu_detail(request, pk):
    edus = Education.objects.all()
    page = Page.objects.all()
    footers = Footer.objects.all()
    socsetis = SocSeti.objects.all()
    return render(request, 'edu_detail.html', {'edu': Education.objects.get(id=pk), 'edus': edus, 'page': page, 'footers': footers, 'socsetis': socsetis})


def page_detail(request, pk):
    edus = Education.objects.all()
    pages = Page.objects.all()
    page = Page.objects.get(id=pk)
    print(page.categories.all())
    footers = Footer.objects.all()
    socsetis = SocSeti.objects.all()
    return render(request, 'page_detail.html', {'pages': page, 'edu': page.category, 'edus': edus, 'page': pages, 'footers': footers, 'socsetis': socsetis})


def blank_detail(request, pk):
    edus = Education.objects.all()
    pages = Page.objects.all()
    page = Blank.objects.get(id=pk)
    footers = Footer.objects.all()
    socsetis = SocSeti.objects.all()
    return render(request, 'blank_detail.html', {'pages': page, 'edus': edus, 'page': pages, 'footers': footers, 'socsetis': socsetis})


def teachers_list(request, pk):
    teachers = Teacher.objects.filter(education=pk)
    edus = Education.objects.all()
    edu = Education.objects.get(id=pk)
    page = Page.objects.all()
    footers = Footer.objects.all()
    socsetis = SocSeti.objects.all()
    return render(request, 'teacher_list.html', {'edu': edu, 'edus': edus, 'teachers': teachers,'page': page, 'footers': footers, 'socsetis': socsetis})

def courses_list(request, pk):
    courses = Course.objects.filter(education=pk)
    edus = Education.objects.all()
    edu = Education.objects.get(id=pk)
    page = Page.objects.all()
    footers = Footer.objects.all()
    socsetis = SocSeti.objects.all()
    return render(request, 'courses_list.html', {'edu': edu, 'edus': edus, 'courses': courses, 'page': page, 'footers': footers, 'socsetis': socsetis})

def ads_detail(request, pk):
    ads = Ads.objects.get(id=pk)
    edus = Education.objects.all()
    footers = Footer.objects.all()
    socsetis = SocSeti.objects.all()
    return render(request, 'ads_detail.html', {'ads': ads, 'edus': edus, 'footers': footers, 'socsetis': socsetis})

def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    edus = Education.objects.all()
    edu = Education.objects.get(id=course.education.pk)
    page = Page.objects.all()
    footers = Footer.objects.all()
    socsetis = SocSeti.objects.all()

    return render(request, 'course_detail.html', {'course': course, 'edu': edu, 'edus': edus, 'page': page, 'footers': footers, 'socsetis': socsetis})



