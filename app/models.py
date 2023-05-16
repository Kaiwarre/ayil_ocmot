from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator


class Education(models.Model):
    title = models.CharField(max_length=123)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Раздел')
        verbose_name_plural = _("Разделы")


class Page(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey('Education', on_delete=models.CASCADE, related_name='edu_pages', blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='images/stat/')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Страница')
        verbose_name_plural = _("Страницы")


class Category(models.Model):
    title = models.CharField(max_length=255)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title


class Ads(models.Model):
    title = models.CharField(max_length=155, verbose_name=_('Название Объявления'))
    description = models.TextField(blank=True, null= True, verbose_name=_('Описание'))
    body = RichTextUploadingField(blank=True, null=True,verbose_name=_('Содержимое объявления'))
    image = models.ImageField(upload_to='images/ads/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Обьявление')
        verbose_name_plural = _("Обьявления")


class Anons(models.Model):
    title = models.CharField(max_length=155, verbose_name=_('Название Анонса'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to='images/anons/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Анонс')
        verbose_name_plural = _("Анонсы")


class Document(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title