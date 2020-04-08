from rest_framework import serializers
from .models import Category

class CategoriesSeializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('id', 'name')