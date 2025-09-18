from django.contrib import admin
from .models import Order, OrderItem, Address, RMA
admin.site.register(Order); admin.site.register(OrderItem); admin.site.register(Address); admin.site.register(RMA)
