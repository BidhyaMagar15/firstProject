from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

from .models import Activity
from .serializers import ActivitySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset= Activity.objects.all()
    serializer_class =ActivitySerializer

    


