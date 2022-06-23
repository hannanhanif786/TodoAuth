from base.serializers import TaskSerializer, CreateSerializer
from .models import Task
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# view for create and read data
class TaskList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        print("user" ,request.user)
        snippets = Task.objects.filter(user= request.user)
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        print(user)
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for update and delete
class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        snippet = Task.objects.get(Q(pk=pk) & Q(user = request.user))
        serializer = CreateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = Task.objects.get(Q(pk=pk) & Q(user = request.user))
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
