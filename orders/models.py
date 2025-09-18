from django.db import models
from catalog.models import Variant, Product
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses", null=True, blank=True)
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=80)
    zone = models.CharField(max_length=80, blank=True)
    address_line = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True)

class Order(models.Model):
    STATUS = [("new","Nuevo"),("paid","Pagado"),("shipped","Enviado"),("delivered","Entregado"),("cancelled","Cancelado")]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class RMA(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="rmas")
    state = models.CharField(max_length=20, default="abierto")
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)