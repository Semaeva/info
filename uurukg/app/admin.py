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
admin.site.register(Category, CategoryAdmin)

admin.site.register(GovnoImage)
admin.site.register(Govno)
admin.site.register(Post)
