from django.shortcuts import render, redirect
# import product form so we can use product form in views
from .forms import TaskForm
from .models import Task
from django.views.decorators.http import require_POST


# READ operation of CRUD
def view_tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)


@require_POST
def add_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        new_task = Task(task_item=request.POST['task_item'])
        new_task.save()

    return redirect('view_tasks')
