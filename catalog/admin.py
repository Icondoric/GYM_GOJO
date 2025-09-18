from django.contrib import admin
from .models import Brand, Category, Product, Variant, ProductMedia, Ingredient, Spec, Bundle, CompareList

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1

class MediaInline(admin.TabularInline):
    model = ProductMedia
    extra = 1

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0

class SpecInline(admin.TabularInline):
    model = Spec
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    inlines = [VariantInline, MediaInline, IngredientInline, SpecInline]
    list_display = ("name","brand","category","is_active")

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Bundle)
admin.site.register(CompareList)