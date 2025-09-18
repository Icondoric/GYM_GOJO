from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, Address
from cart.views import _get_cart
from django.db import transaction
from decimal import Decimal

@login_required(login_url="/accounts/login/")
def checkout(request):
    cart = _get_cart(request)
    if request.method == "POST":
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        city = request.POST.get("city","")
        address_line = request.POST.get("address_line","")
        addr = Address.objects.create(full_name=name, phone=phone, city=city, address_line=address_line)
        with transaction.atomic():
            order = Order.objects.create(address=addr, total=Decimal("0.00"), user=request.user)
            total = Decimal("0.00")
            for item in cart.items.select_related("variant"):
                OrderItem.objects.create(order=order, variant=item.variant, qty=item.qty, price=item.variant.price)
                total += item.variant.price*item.qty
            order.total = total
            order.save()
            cart.items.all().delete()
        return redirect("order_success", order_id=order.id)
    return render(request,"orders/checkout.html", {"cart": cart})

@login_required(login_url="/accounts/login/")
def success(request, order_id):
    return render(request, "orders/success.html", {"order_id": order_id})
