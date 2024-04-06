from django.contrib import admin
from .models import Product, Category, Genders, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'gender',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class GendersAdmin(admin.ModelAdmin):
    list_display = (
        'gender_friendly_name',
        'name',
    )      


class ReviewyAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
        'content',
    )    


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genders, GendersAdmin)
admin.site.register(Review, ReviewyAdmin)
