from modeltranslation.translator import translator, TranslationOptions
from .models import Post, Category, Press_release, NewsSNG, Department, Country, Govno


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'overview', 'description',)


class Press_releaseTranslationOptions(TranslationOptions):
    fields = ('title', 'overview', 'description', )


class NewsSNGTranslationOptions(TranslationOptions):
    fields = ('title', 'overview',  'description', )


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('title', )


class CountryTranslationOptions(TranslationOptions):
    fields = ('title', )


class GovnoTranslationOptions(TranslationOptions):
    fields = ('position', 'department', 'resume', 'dop_info', 'years',)


translator.register(Post, PostTranslationOptions)
translator.register(Press_release, Press_releaseTranslationOptions)
translator.register(NewsSNG, NewsSNGTranslationOptions)
translator.register(Country, CountryTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(Govno, GovnoTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
