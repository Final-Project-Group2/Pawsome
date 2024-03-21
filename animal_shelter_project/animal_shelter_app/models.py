from django.db import models
from django.contrib.auth.models import AbstractUser
from user_managment_app.models import CustomUser, Shelter

# Create your models here.

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat')
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large')
    ]

    STATUS_CHOICES = [
        ('adoptable', 'Adoptable'),
        ('pending_adoption', 'Pendingadoption'),
        ( 'adopted', 'Adopted')
    ]

    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    breeds = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    weight = models.CharField(max_length=50)
    photos = models.ImageField(upload_to='pets_images')
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.species})"
    
class Application(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"{self.user} ({self.pet})"
    
    def save(self, *args, **kwargs):
        self.pet.status = 'pending_adoption'
        self.pet.save()
        super().save(*args, **kwargs)

