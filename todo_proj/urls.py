from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()
router.register('todo', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
