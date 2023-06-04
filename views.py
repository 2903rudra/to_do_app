from django.shortcuts import render
from rest_framework import viewsets
from.models import Task
from.serializers import TaskSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class TaskViewset (viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

