from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class AdoptionPreference(models.Model):
    PET_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]

    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    AGE_CHOICES = [
        ('any', 'Any Age'),
        ('young', 'Young (0-2 years)'),
        ('adult', 'Adult (3-8 years)'),
        ('senior', 'Senior (9+ years)'),
    ]

    ACTIVITY_CHOICES = [
        ('high', 'High-energy'),
        ('medium', 'Medium-energy'),
        ('low', 'Low-energy'),
    ]

    TEMPERAMENT_CHOICES = [
        ('playful', 'Playful'),
        ('affectionate', 'Affectionate'),
        ('independent', 'Independent'),
    ]

    GROOMING_CHOICES = [
        ('high', 'High maintenance'),
        ('low', 'Low maintenance'),
    ]

    ENVIRONMENT_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House with a yard'),
    ]

    TIME_CHOICES = [
        ('1', '1 hour or less'),
        ('2', '1-2 hours'),
        ('3', '2-3 hours'),
        ('4', '3+ hours'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet_type = models.CharField(verbose_name='Pet Type', choices=PET_CHOICES, max_length=10)
    breed_preference = models.CharField(verbose_name='Breed Preference', max_length=250)
    size = models.CharField(verbose_name='Size', choices=SIZE_CHOICES, max_length=10)
    age = models.CharField(verbose_name='Age', choices=AGE_CHOICES, max_length=10)
    activity_level = models.CharField(verbose_name='Activity Level', choices=ACTIVITY_CHOICES, max_length=10)
    temperament = models.CharField(verbose_name='Temperament', choices=TEMPERAMENT_CHOICES, max_length=15)
    compatibility_with_other_pets_or_children = models.CharField(verbose_name='Compatibility with Other Pets or Children', max_length=250)
    grooming_needs = models.CharField(verbose_name='Grooming Needs', choices=GROOMING_CHOICES, max_length=10)
    living_environment = models.CharField(verbose_name='Living Environment', choices=ENVIRONMENT_CHOICES, max_length=10)
    time_commitment = models.CharField(verbose_name='Time Commitment', choices=TIME_CHOICES, max_length=1)


    def __str__(self):
        return f"Adoption Preferences for {self.user.username}"
