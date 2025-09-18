from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import HomeView, LegalView, MembershipsView, AccountDashboardView  # <-- añade AccountDashboardView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("legal/<slug:slug>/", LegalView.as_view(), name="legal"),
    path("memberships/", MembershipsView.as_view(), name="memberships"),

    # 👇 NUEVO: perfil de usuario
    path("accounts/profile/", AccountDashboardView.as_view(), name="account_profile"),

    path("catalog/", include("catalog.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("reviews/", include("reviews.urls")),
    path("blog/", include("blog.urls")),
    path("promotions/", include("promotions.urls")),
    path("subscriptions/", include("subscriptions.urls")),
    path("search/", include("searchapp.urls")),
    path("accounts/", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
