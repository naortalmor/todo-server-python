from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializers

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()
