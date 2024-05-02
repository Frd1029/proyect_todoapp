from django.shortcuts import render

# Create your views here.
from .models import Task, User
from django.http import JsonResponse
from django.core.serializers import serialize


def tasks_list(request):
    tasks = Task.objects.all()
    data = serialize('python', tasks)
    return JsonResponse(data, safe=False)
    


def users_list(request):
    users = User.objects.all()
    data = serialize('python', users)
    return JsonResponse(data, safe=False)
