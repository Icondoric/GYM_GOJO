from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product
from orders.models import Order

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["top_sellers"] = Product.objects.filter(is_active=True)[:8]
        ctx["brands"] = ["GOYO","Titan","PowerFuel","IronWear"]
        return ctx

class LegalView(TemplateView):
    template_name = "legal.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["slug"] = kwargs.get("slug","")
        return ctx

class MembershipsView(TemplateView):
    template_name = "memberships.html"

# 👇 NUEVO: Dashboard “Mi cuenta”
class AccountDashboardView(LoginRequiredMixin, TemplateView):
    login_url = "/accounts/login/"
    template_name = "account/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["orders"] = Order.objects.filter(user=self.request.user).order_by("-created_at")[:10]
        return ctx
