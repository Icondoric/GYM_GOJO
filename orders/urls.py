from django.urls import path
from .views import checkout, success
urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("success/<int:order_id>/", success, name="order_success"),
]