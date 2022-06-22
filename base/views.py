from rest_framework.response import Response
from rest_framework import generics
from base.serializers import TaskSerializer
from .models import Task
from rest_framework.views import APIView

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# class TaskList(APIView):
#     def get(self, request, format=None):
#         snippets = Task.objects.all()
#         serializer = TaskSerializer(snippets, many=True)
#         return Response(serializer.data)

