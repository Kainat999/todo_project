from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='todo_app/login.html'), name='login'),
    
    path('todo/', views.todo_list, name='todo_list'),
    path('add/', views.add_todo_item, name='add_todo_item'),
    path('delete/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),

]
