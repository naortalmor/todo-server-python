from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404


# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()

    @action(detail=False, methods=['POST'], name="bla")
    def delete_some(self, request):
        queryset = self.get_queryset()
        try:
            for task_id in self.request.data:
                task = queryset.filter(pk=task_id)
                task.delete()
        except:
            raise Http404('Failed to delete')
        return Response({'ok': 'ok'})
