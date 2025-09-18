from django.db import models
from django.urls import reverse
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=90, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    def __str__(self): return self.name

class Product(models.Model):
    SKU_TYPES = [("simple","Simple"),("variant","Con variantes")]
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    sku_type = models.CharField(max_length=10, choices=SKU_TYPES, default="variant")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse("pdp", args=[self.slug])
    @property
    def price_min(self):
        variant = self.variants.order_by("price").first()
        return variant.price if variant else None

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    sku = models.CharField(max_length=50, unique=True)
    flavor = models.CharField(max_length=50, blank=True)  # for supplements
    size = models.CharField(max_length=20, blank=True)    # for apparel
    color = models.CharField(max_length=20, blank=True)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    def __str__(self): return f"{self.product.name} - {self.sku}"

class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="media")
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    video_url = models.URLField(blank=True)
    alt = models.CharField(max_length=120, blank=True)

class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=120)
    amount = models.CharField(max_length=60, blank=True) # e.g., 25g
    def __str__(self): return f"{self.name} {self.amount}".strip()

class Spec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specs")
    name = models.CharField(max_length=120) # e.g., carga máxima
    value = models.CharField(max_length=120)

class Bundle(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    products = models.ManyToManyField(Product, related_name="bundles")
    discount_percent = models.PositiveIntegerField(default=10)
    is_active = models.BooleanField(default=True)

class CompareList(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)
    products = models.ManyToManyField(Product, blank=True)