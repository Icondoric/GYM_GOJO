from django.contrib import admin
from django.utils.html import format_html
from .models import Brand, Category, Product, Variant, ProductMedia, Ingredient, Spec, Bundle, CompareList

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1

class MediaInline(admin.TabularInline):
    model = ProductMedia
    fields = ("preview", "image", "alt", "is_primary", "video_url")
    readonly_fields = ("preview",)
    extra = 1

    def preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image.url)
        return "—"

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
    list_display = ("name","brand","category","is_active","primary_thumb")
    list_filter = ("is_active","brand","category")
    search_fields = ("name","slug","description","brand__name")

    def primary_thumb(self, obj):
        pm = obj.primary_media()
        if pm and pm.image:
            return format_html('<img src="{}" style="height:40px;border-radius:6px;" />', pm.image.url)
        return "—"
    primary_thumb.short_description = "Imagen"

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Bundle)
admin.site.register(CompareList)
