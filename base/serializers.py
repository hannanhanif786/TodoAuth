from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['user']
