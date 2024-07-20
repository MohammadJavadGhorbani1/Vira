from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['title']}

class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['title']}

admin.site.register(ArticleModel , ArticleAdmin)
admin.site.register(ArticleCategoryModel)
admin.site.register(ArticleTagModel , ArticleTagAdmin)
