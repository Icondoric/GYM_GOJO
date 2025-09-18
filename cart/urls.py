from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart

app_name = "cart"

urlpatterns = [
    path("", view_cart, name="cart_view"),
    path("add/<int:variant_id>/", add_to_cart, name="cart_add"),
    path("remove/<int:item_id>/", remove_from_cart, name="cart_remove"),
]
