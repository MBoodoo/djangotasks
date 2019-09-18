from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TasksSerializer
from .models import Tasks

# Create your views here.

# inheriting viewsets.ModelViewSet allows us 
# to specify a "serializer class" to use later
# from the serialzer file that was created using 
# the rest_framework package

class TasksView(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()