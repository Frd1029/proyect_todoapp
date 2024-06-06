from rest_framework import serializers
from .models import Task


class TasksCreateSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = ["title", "description", "status", "deadline", "priority"]

    def create(self, validated_data):
        validated_data['user'] =self.context['request'].user
        return super(TasksCreateSerializer, self).create(validated_data)

class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']
        
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status')
        instance.save()
        return instance
