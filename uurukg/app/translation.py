from modeltranslation.translator import translator, TranslationOptions
from .models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'overview', 'description', )  # Specify the fields you want to translate for the Post model


translator.register(Post, PostTranslationOptions)