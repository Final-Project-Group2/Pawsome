from django import forms
from .models import CustomUser, Shelter

from django import forms
from .models import CustomUser, Shelter

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'street_address', 'city', 'country', 'image']

class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['name', 'street_address', 'city', 'country', 'email', 'phone_number', 'image', 'website', 'description']