from rest_framework import serializers
from .models import Task


class TasksCreateSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = ["title", "description", "status", "deadline", "priority"]

    def create(self, validated_data):
        validated_data['user'] =self.context['request'].user
        return super(TasksCreateSerializer, self).create(validated_data)

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "deadline", "priority"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance

class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']
        
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status')
        instance.save()
        return instance

class TaskDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        try:
            task = Task.objects.get(pk=value)
        except Task.DoesNotExist:
            raise serializers.ValidationError("Task not found")
        return value

    def delete(self, validated_data):
        task = Task.objects.get(pk=validated_data['id'])
        task.delete()
        return task
