from django.shortcuts import render

# Create your views here.
from .models import Task, User


def tasks_list(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "tasks/index.html", context)


def users_list(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "users/index.html", context)
