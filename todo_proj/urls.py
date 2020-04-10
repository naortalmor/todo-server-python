from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo import views as todo_views
from categories import views as cat_views
from login import views as login_views

router = DefaultRouter()
router.register('todo', todo_views.TodoView, 'todo')
router.register('categories', cat_views.CategoriesView, 'categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', login_views.LoginUsers.as_view())
]
