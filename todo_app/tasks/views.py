
# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from .models import Task
from .serializers import TasksCreateSerializer, TaskStatusUpdateSerializer, TaskDeleteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksCreateSerializer
    filter_backends = [OrderingFilter]
    ordening_fields = ["priority"]

    def get_queryset(self):
        return self.request.user.tasks.all()

    def partial_update(self, request, pk):
        queryset = self.get_queryset()
        task = queryset.get(pk=pk)
        serializer = TaskStatusUpdateSerializer(data=request.data, instance=task, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
            
    def destroy(self, request, pk=None):
        serializer = TaskDeleteSerializer(data={'id': pk})
        serializer.is_valid(raise_exception=True)
        queryset = self.get_queryset()
        task = queryset.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        