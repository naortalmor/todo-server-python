from rest_framework import serializers
from .models import Category

class CategoriesSeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'user_id')