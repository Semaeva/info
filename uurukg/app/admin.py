from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('title',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = 'Панель администратора UURUKG'
admin.site.index_title = 'UURUKG'

# admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(Country)
admin.site.register(Category, CategoryAdmin)

admin.site.register(GovnoImage)
admin.site.register(NewsSNG)
admin.site.register(NewsSngImage)
admin.site.register(PressReleaseImage)
admin.site.register(Govno)
admin.site.register(Post)
admin.site.register(Press_release)
admin.site.register(Department)
