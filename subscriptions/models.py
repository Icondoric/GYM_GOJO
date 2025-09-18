from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Subscription(models.Model):
    PERIODS = [("monthly","Mensual"),("quarterly","Trimestral")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    period = models.CharField(max_length=20, choices=PERIODS, default="monthly")
    active = models.BooleanField(default=True)
    next_charge = models.DateField(null=True, blank=True)