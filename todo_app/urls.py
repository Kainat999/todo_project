from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo_item, name='add_todo_item'),
    path('delete/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),

]
