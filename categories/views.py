from rest_framework import viewsets
from .models import Category
from .serializers import CategoriesSeializer
from rest_framework.response import Response


# Create your views here.
class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSeializer
    queryset = Category.objects.all()

    def list(self, request):
        userid = self.request.query_params.get('userid', None)
        if userid is not None:
            queryset = self.get_queryset().filter(user_id=userid)
            serialize = self.get_serializer(queryset, many=True)
            return Response(serialize.data)
        else:
            return Response([])