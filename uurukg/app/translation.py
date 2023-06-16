from modeltranslation.translator import translator, TranslationOptions
from .models import Post, Category, Press_release, NewsSNG, Department, Country, Govno


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'overview', 'description', 'category', )  # Specify the fields you want to translate for the Post model


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


class Press_releaseTranslationOptions(TranslationOptions):
    fields = ('title', 'overview', 'departments', 'description', )


class NewsSNGTranslationOptions(TranslationOptions):
    fields = ('title', 'overview', 'sng', 'description', )


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('title', )


class CountryTranslationOptions(TranslationOptions):
    fields = ('title', )


class GovnoTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'department', 'resume', 'dop_info', 'criminal_record', 'years',)


translator.register(Post, PostTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Press_release, Press_releaseTranslationOptions)
translator.register(NewsSNG, NewsSNGTranslationOptions)
translator.register(Country, CountryTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(Govno, GovnoTranslationOptions)