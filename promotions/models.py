from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    percent_off = models.PositiveIntegerField(default=10)
    active = models.BooleanField(default=True)

class GiftCard(models.Model):
    code = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)