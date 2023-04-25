from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator


class Education(models.Model):
    title = models.CharField(max_length=123)
    body = RichTextUploadingField(blank=True, null=True)
    # image = models.ImageField(upload_to='images/stat/')
    description = models.TextField()
    # skEditor .RichUploader

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


class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_('Полное имя'))
    content = RichTextUploadingField(blank=True, null=True,verbose_name=_('Описание'))
    date = models.DateTimeField(auto_now_add=True)
    exp = models.IntegerField(verbose_name=_('Опыт работы'))
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/employee/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _("Сотрудники")


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


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название курса'))
    content = RichTextUploadingField(blank=True, null=True, verbose_name=_('Описание'))
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/teacher/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Направление')
        verbose_name_plural = _("Направлении")


class EduImages(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    image = models.ImageField(upload_to='images/')
    edu = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='edu_images', blank=True, null=True)

    def __str__(self):
        return f'{self.edu} - {self.pk}'

    class Meta:
        verbose_name = 'Картинки на слайде'
        verbose_name_plural = 'Картинки на слайде'


class Category(models.Model):
    title = models.CharField(max_length=255)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title


class Blank(models.Model):
    title = models.CharField(max_length=128)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/stat/', blank=True, null=True)
    page = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blanks_cat')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Страница на странице'
        verbose_name_plural = 'Страницы на странице'


class Footer(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class SocSeti(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title
