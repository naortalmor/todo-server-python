from rest_framework import viewsets
from .models import Category
from .serializers import CategoriesSeializer

# Create your views here.
class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSeializer
    queryset = Category.objects.all()