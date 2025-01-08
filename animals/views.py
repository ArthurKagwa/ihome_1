from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .models import Animal, Breed, Type, Staff, Event, Task
from .serializers import AnimalSerializer, BreedSerializer, TypeSerializer, StaffSerializer, EventSerializer, TaskSerializer

class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

def home(request):
    return HttpResponse('Welcome to the Animal  API')

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


