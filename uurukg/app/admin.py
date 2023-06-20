from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Press_release, NewsSNG, NewsImage, Category, Country, PressReleaseImage, GovnoImage, \
    NewsSngImage, Govno, Department
from .translation import PostTranslationOptions


# галерея -------------------------//--------------------------------------
class PostImageAdmin(admin.StackedInline):
    model = NewsImage


@admin.register(Post)
class PostsAdmin(TranslationAdmin):
    list_display = ('title',)

    inlines = [PostImageAdmin]

    class Meta:
        model = Post


class NewsSNGImageAdmin(admin.StackedInline):
    model = NewsSngImage


@admin.register(NewsSNG)
class NewsSNGAdmin(TranslationAdmin):
    list_display = ('title',)
    inlines = [NewsSNGImageAdmin]

    class Meta:
        model = NewsSNG


class GovnoImageAdmin(admin.StackedInline):
    model = GovnoImage


@admin.register(Govno)
class GovnoAdmin(TranslationAdmin):
    list_display = ('name', 'resume',)
    inlines = [GovnoImageAdmin]


class PressReleaseImageAdmin(admin.StackedInline):
    model = PressReleaseImage


@admin.register(Press_release)
class PressRealeaseAdmin(TranslationAdmin):
    list_display = ('title',)
    inlines = [PressReleaseImageAdmin]


@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ('title',)


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('title',)
    list_display = ('title',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = 'Панель администратора UURUKG'
admin.site.index_title = 'UURUKG'

# admin.site.register(NewsImage)
# admin.site.register(GovnoImage)
# admin.site.register(NewsSngImage)
# admin.site.register(PressReleaseImage)


