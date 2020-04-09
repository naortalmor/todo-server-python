from rest_framework import serializers
from .models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'header', 'description', 'is_done', 'creation_date', 'due_date', 'category_id')
