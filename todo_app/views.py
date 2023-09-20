from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todo_items': todo_items})

def add_todo_item(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    return render(request, 'todo_app/add_todo_item.html', {'form': form})

def delete_todo_item(request, todo_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_id)
    todo_item.delete()
    return redirect('todo_list')