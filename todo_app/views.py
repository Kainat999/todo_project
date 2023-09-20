
# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoForm



@login_required
def todo_list(request):
    todo_items = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo_app/todo_list.html', {'todo_items': todo_items})




@login_required
def add_todo_item(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    return render(request, 'todo_app/add_todo_item.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'todo_app/register.html', {'form': form})



def delete_todo_item(request, todo_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_id)
    todo_item.delete()
    return redirect('todo_list')