import modeltranslation.translator
from modeltranslation.translator import register, TranslationOptions
from .models import Education, Page, Ads, Anons, Course, Blank


@register(Education)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'description')


@register(Page)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'description')


@register(Ads)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'body')


@register(Blank)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'body')


@register(Anons)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Course)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')