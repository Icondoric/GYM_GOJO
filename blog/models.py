from django.db import models
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=170, unique=True)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    cover = models.ImageField(upload_to="blog/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self): return reverse("blog_detail", args=[self.slug])
    def __str__(self): return self.title