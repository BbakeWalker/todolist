from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    path('deleteCompleted', views.deleteCompleted, name='delete_completed'),
    path('deleteAll', views.deleteAll, name='delete_all')
]
