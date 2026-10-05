from django.shortcuts import render
from rest_framework import viewssets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewssets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer

    


