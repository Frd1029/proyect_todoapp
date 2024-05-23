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

    def create(self, validated_data):
        validated_data['user'] =self.context['request'].user
        return super(TasksSerializer, self).create(validated_data)