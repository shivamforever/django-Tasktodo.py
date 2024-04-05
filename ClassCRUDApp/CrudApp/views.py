from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator


def goHome(request):
    Tasks = TaskModel.objects.all()
    # search
    if request.method == 'GET':
        search_title = request.GET.get('search_title')
        if search_title != None:
            Tasks = TaskModel.objects.filter(title__contains=search_title)

    # pagination
    paginator = Paginator(Tasks, 5)
    page = request.GET.get('page')
    FinalTasks = paginator.get_page(page)

    data = {
        'title': 'Home Page',
        'tasks': FinalTasks,
    }
    return render(request, 'index.html', data)


def goAdd(request):
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            due_date = request.POST.get('due_date')

            form = TaskModel(
                title=title,
                due_date=due_date,
                is_completed=False
            )
            form.save()

            return redirect('/')

    except Exception as e:
        print(e)

    return redirect('/')


def goUpdate(request, id):
    try:
        if request.method == 'POST':
            title = request.POST.get('update_title')
            due_date = request.POST.get('update_due_date')
            is_completed = bool(request.POST.get('update_is_completed', False))

            form = TaskModel.objects.get(id=id)
            form.title = title
            form.due_date = due_date
            form.is_completed = is_completed
            form.save()

            # form = TaskModel(
            #     id = id,
            #     title = title,
            #     assigned_date = assigned_date,
            #     due_date = due_date,
            #     is_completed = is_completed
            # )
            # form.save()

            return redirect('/')

    except Exception as e:
        print(e)

    return redirect('/')


def toggle_complete(request, id):
    try:
        task = TaskModel.objects.get(id=id)
        task.is_completed = not task.is_completed
        task.save()
    except Exception as e:
        print(e)

    return redirect('/')


def goDelete(request, id):
    try:
        TaskModel.objects.get(id=id).delete()

    except Exception as e:
        print(e)

    return redirect('/')
