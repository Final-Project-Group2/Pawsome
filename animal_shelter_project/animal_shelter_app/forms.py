from django import forms
from .models import Pet, Application
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class AddPetForm(forms.ModelForm):  
    class Meta:
        model = Pet
        exclude = ['status', 'published_at', 'updated_at', 'shelter'] 
                

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        self.fields['species'].widget = forms.Select(choices=Pet.SPECIES_CHOICES)
        self.fields['gender'].widget = forms.Select(choices=Pet.GENDER_CHOICES)
        self.fields['size'].widget = forms.Select(choices=Pet.SIZE_CHOICES)
        
        
    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.status = 'adoptable'
        pet.published_at = timezone.now()
        pet.updated_at = timezone.now()
        
        if commit:
            pet.save()
        return pet


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['message']
