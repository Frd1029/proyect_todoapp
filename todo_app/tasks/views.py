from django.shortcuts import render

# Create your views here.
from .models import Task
from django.http import JsonResponse
from django.core.serializers import serialize
from .serializers import TasksSerializer

from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
