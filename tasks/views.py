from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            default_tasks = [
                {'id': 1, 'title': 'Task 1', 'description': 'Hi I am the placeholder'}
            ]
            return Response(default_tasks)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
