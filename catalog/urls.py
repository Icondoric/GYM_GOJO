from django.urls import path
from .views import CategoryPLP, ProductPDP, compare_toggle

urlpatterns = [
    path("c/<slug:slug>/", CategoryPLP.as_view(), name="plp"),
    path("p/<slug:slug>/", ProductPDP.as_view(), name="pdp"),
    path("compare/toggle/<int:pk>/", compare_toggle, name="compare_toggle"),
]