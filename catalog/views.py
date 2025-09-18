from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product, Brand, Variant, Bundle
from django.db.models import Q

class CategoryPLP(ListView):
    template_name = "catalog/plp.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        qs = Product.objects.filter(category=self.category, is_active=True).select_related("brand","category")
        q = self.request.GET.get("q")
        brand = self.request.GET.get("brand")
        objetivo = self.request.GET.get("objective")
        tipo = self.request.GET.get("type")
        flavor = self.request.GET.get("flavor")
        size = self.request.GET.get("size")
        stock = self.request.GET.get("stock")
        if q: qs = qs.filter(Q(name__icontains=q)|Q(description__icontains=q))
        if brand: qs = qs.filter(brand__slug=brand)
        if objetivo: qs = qs.filter(description__icontains=objetivo)
        if tipo: qs = qs.filter(description__icontains=tipo)
        if flavor: qs = qs.filter(variants__flavor__iexact=flavor)
        if size: qs = qs.filter(variants__size__iexact=size)
        if stock == "in": qs = qs.filter(variants__stock__gt=0)
        return qs.distinct()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        ctx["brands"] = Brand.objects.all()
        return ctx

class ProductPDP(DetailView):
    template_name = "catalog/pdp.html"
    model = Product
    slug_field = "slug"
    slug_url_kwarg = "slug"

def compare_toggle(request, pk):
    product = get_object_or_404(Product, pk=pk)
    session_key = request.session.session_key or request.session.create()
    from .models import CompareList
    cl, _ = CompareList.objects.get_or_create(session_key=request.session.session_key)
    if product in cl.products.all():
        cl.products.remove(product)
    else:
        cl.products.add(product)
    return redirect(request.META.get("HTTP_REFERER","/"))