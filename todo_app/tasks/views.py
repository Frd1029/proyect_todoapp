
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action  # To filter completeds
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from .models import Task
from .serializers import TasksSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [OrderingFilter]
    ordening_fields = ["priority"]

    def get_queryset(self):
        return self.request.user.tasks.all()

# Modification to filter by completed
    @action(detail=False, methods=['get'])
    def completed_tasks(self, request):
        completed_tasks = self.get_queryset().filter(status="COMPLETED")
        serializer = self.get_serializer(completed_tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pending_tasks(self, request):
        pending_tasks = self.get_queryset().filter(status="PENDING")
        serializer = self.get_serializer(pending_tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def order_tasks_priority(self, request):
        order_tasks_priority = self.get_queryset().order_by("-priority")
        serializer = self.get_serializer(order_tasks_priority, many=True)
        return Response(serializer.data)