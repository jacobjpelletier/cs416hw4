from django.shortcuts import render, redirect
# import product form so we can use product form in views
from .forms import TaskForm
from .models import Task


# READ operation of CRUD
def view_tasks(request):
    # get all tasks
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    form = TaskForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        # after saving redirect to view_product page
        return render(request, 'tasks/index.html', context)

    # if the request does not have post data, a blank form will be rendered
    # return render(request, 'tasks/index.html', {'form': form})
    return render(request, 'tasks/index.html', context)

