from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author']
    prepopulated_fields = {'slug' : ['title']}
    exclude = ['author']
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            return super(ArticleAdmin, self).save_model(request, obj, form, change)
        else:
            pass


class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['title']}

admin.site.register(ArticleModel , ArticleAdmin)
admin.site.register(ArticleCategoryModel)
admin.site.register(ArticleTagModel , ArticleTagAdmin)
admin.site.register(ArticleCommentModel)
