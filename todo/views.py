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

    @action(detail=False, methods=['POST'], name="delete some")
    def delete_some(self, request):
        queryset = self.get_queryset()
        try:
            for task_id in self.request.data:
                task = queryset.filter(pk=task_id)
                task.delete()
        except:
            raise Http404('Failed to delete')
        return Response({'ok': 'ok'})

    @action(detail=True, methods=['POST'], name="toggleDone")
    def toggle_done(self, request, pk=None):
        task = self.get_object()
        task.is_done = not task.is_done
        task.save()
        return Response({'ok', 'ok'})