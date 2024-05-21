from django.shortcuts import render

# Create your views here.
from .models import Task
from django.http import JsonResponse
from django.core.serializers import serialize
from .serializers import TasksSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [OrderingFilter]
    ordening_fields = ["priority"]

    def get_queryset(self):
        return self.request.user.tasks.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        data["user"] = self.request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CRATED, headers=headers)
