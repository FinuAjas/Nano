from django.contrib import admin
from . models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category','slug','cat_images')
    prepopulated_fields = {'slug':('category',)}

admin.site.register(Category , CategoryAdmin)

