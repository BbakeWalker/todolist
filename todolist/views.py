from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    #return render(request, 'todolist/index.html')
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items' : todo_items, 'form' : form}
    return render(request, 'todolist/index.html', context)

#view decorators can be use to restrict access to certain views
#Django comes with some built-in decorators e.g. login_required, require_POST

#requore_POST restrict access to the addTodoItem view by allowing POST only
@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    #adding to the database
    if form.is_valid():
        new_todo = Todolist(text = request.POST['text'])
        new_todo.save()

    #displaying in the consol
    #print(request.POST['text'])

    #redirecting back to the index
    return redirect('index')

def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact = True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')
