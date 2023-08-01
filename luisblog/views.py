from rest_framework import viewsets, filters, permissions
from .serializer import BlogSerializer
from .models import Blog

class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'contenido']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]