from django.shortcuts import render
from catalog.models import Product
from django.db.models import Q

def search(request):
    q = request.GET.get("q","")
    syn = {"whey":"proteína","creatina":"creatine"}  # demo synonyms
    q_alt = syn.get(q.lower())
    qs = Product.objects.filter(is_active=True)
    if q:
        qs = qs.filter(Q(name__icontains=q)|Q(description__icontains=q))
        if q_alt:
            qs = qs | Product.objects.filter(Q(name__icontains=q_alt)|Q(description__icontains=q_alt))
    return render(request, "search/results.html", {"q": q, "products": qs.distinct()})