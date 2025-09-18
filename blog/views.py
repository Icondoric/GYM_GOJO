from django.views.generic import ListView, DetailView
from .models import Post

class BlogList(ListView):
    model = Post
    template_name = "blog/list.html"
    paginate_by = 10

class BlogDetail(DetailView):
    model = Post
    template_name = "blog/detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"