from django.contrib import admin
from .models import Animal, Breed, Type, Staff

# Register your models here.
admin.site.register(Animal)
admin.site.register(Breed)
admin.site.register(Type)
admin.site.register(Staff)
