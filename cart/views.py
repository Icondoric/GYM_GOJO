from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from catalog.models import Variant

def _get_cart(request: HttpRequest) -> Cart:
    if not request.session.session_key:
        request.session.create()
    cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

def view_cart(request):
    cart = _get_cart(request)
    return render(request, "cart/cart.html", {"cart": cart})

@login_required(login_url="/accounts/login/")
def add_to_cart(request, variant_id):
    cart = _get_cart(request)
    variant = get_object_or_404(Variant, id=variant_id)
    item, created = CartItem.objects.get_or_create(cart=cart, variant=variant)
    if not created:
        item.qty += 1
        item.save()
    return redirect("cart:cart_view")

@login_required(login_url="/accounts/login/")
def remove_from_cart(request, item_id):
    cart = _get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    return redirect("cart:cart_view")
