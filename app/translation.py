import modeltranslation.translator
from modeltranslation.translator import register, TranslationOptions
from .models import Education, Page, Ads, Anons


@register(Education)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'description')


@register(Page)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'description')


@register(Ads)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'body')



@register(Anons)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


