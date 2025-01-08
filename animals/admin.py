from django.contrib import admin
from .models import Animal, Breed, Type, Staff, Event, Task

# Register your models here.
admin.site.register(Animal)
admin.site.register(Breed)
admin.site.register(Type)
admin.site.register(Staff)
admin.site.register(Event)
admin.site.register(Task)