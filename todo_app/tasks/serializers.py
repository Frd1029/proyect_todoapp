from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        model = Task
        fields = ["title", "description", "status", "user"]
