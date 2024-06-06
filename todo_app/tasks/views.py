
# Create your views here.
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import Task
from .serializers import TasksCreateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksCreateSerializer
    filter_backends = [OrderingFilter]
    ordening_fields = ["priority"]

    def get_queryset(self):
        return self.request.user.tasks.all()

