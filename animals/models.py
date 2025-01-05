from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return "Type: " + self.name + " Description: " + self.desc


class Breed(models.Model):
    breed_origin = models.CharField(max_length=10)
    breed_name = models.CharField(max_length=50)
    breed_description = models.CharField(max_length=500)
    animal_type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Origin: " + self.breed_origin + " Breed: " + self.breed_name + " Description: " + self.breed_description


class Animal(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey('Animal', on_delete=models.SET_NULL, null=True, related_name='animal_mother')
    father = models.ForeignKey('Animal', on_delete=models.SET_NULL, null=True, related_name='animal_father')
    dob = models.DateField()

    def __str__(self):
        return "id: " + self.id + " type: " + self.type.name + " breed: " + self.breed.breed_name + " dob: " + str(self.dob)


class Staff(models.Model):
    staff_id = models.CharField(max_length=10, primary_key=True)
    staff_name = models.CharField(max_length=50)
    staff_address = models.CharField(max_length=100)
    staff_phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")],
    )
    staff_email = models.EmailField()
    staff_position = models.CharField(max_length=50)
    staff_nin = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "Staff ID: " + self.staff_id + " Name: " + self.staff_name + " Position: " + self.staff_position
