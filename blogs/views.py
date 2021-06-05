# Create your views here.
from rest_framework import viewsets

from blogs.models import Blog
from blogs.serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('title')
    serializer_class = BlogSerializer
