from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

from .models import Animal, Breed, Type, Staff, Event, Task, Farm
from .serializers import AnimalSerializer, BreedSerializer, TypeSerializer, StaffSerializer, EventSerializer, \
    TaskSerializer, UserSerializer, MyTokenObtainPairSerializer


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

class UserViewSet(ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = UserSerializer

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        farm_name = request.data.get('farm_name')

        if not username or not password or not email or not farm_name:
            return HttpResponse('Please provide all required fields', status=400)
        if Farm.objects.filter(username=username).exists():
            return HttpResponse('Farm Username already exists', status=400)
        if Farm.objects.filter(email=email).exists():
            return HttpResponse('Farm Email already exists', status=400)

        user = Farm.objects.create_user(username=username, password=password, email=email, farm_name=farm_name)

        return HttpResponse('Farm created successfully', status=201)





