from django.contrib import admin
from . models import Banner, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date')
    prepopulated_fields = {'slug':('product_name',)}

class BannerAdmin(admin.ModelAdmin):
    list_display = ('product_name','banner_image','banner_mainhead','banner_subhead')    


admin.site.register(Product , ProductAdmin)
admin.site.register(Banner , BannerAdmin)
