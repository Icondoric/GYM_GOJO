from django.db import models
from catalog.models import Variant

class Cart(models.Model):
    session_key = models.CharField(max_length=40, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    def subtotal(self): return self.variant.price * self.qty