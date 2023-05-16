from .views import *
from django.urls import path
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', home, name='home'),
    path('education/<int:pk>', edu_detail, name='edu_detail'),
    path('page/<int:pk>', page_detail, name='page_detail'),
    path('ads_detail/<int:pk>', ads_detail, name='ads_detail'),
    path('upload_pdf/', upload_pdf, name='upload_pdf'),
]

