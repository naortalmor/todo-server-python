from rest_framework import serializers
from .models import Todo


class TodoSerializers(serializers.ModelSerializer):
    category_id = serializers.SerializerMethodField('get_category_id')

    def get_category_id(self, obj):
        return obj.category_id.id

    class Meta:
        model = Todo
        fields = ('id', 'header', 'description', 'is_done', 'creation_date', 'due_date', 'category_id')
