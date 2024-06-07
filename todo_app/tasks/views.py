
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