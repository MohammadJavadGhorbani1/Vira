from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title' , 'price' , 'off' , 'is_active']
    list_editable = ['price' , 'off' , 'is_active']
    list_filter = ['is_active']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title']

class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title']

admin.site.register(Products , ProductAdmin)
admin.site.register(ProductCategory , CategoryAdmin)
admin.site.register(ProductTags , TagsAdmin)