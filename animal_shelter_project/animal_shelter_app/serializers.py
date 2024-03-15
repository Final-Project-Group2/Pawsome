from rest_framework import serializers
from .models import Pet, Shelter, Application
from django.core.validators import validate_email

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['id', 'name', 'street_address', 'city', 'country', 'email', 'phone_number', 'image', 'website', 'description']

        def validate_email(self, value):
            try:
                validate_email(value)
            except ValueError as e:
                raise serializers.ValidationError(str(e))
            return value
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'breeds', 'age', 'gender', 'size', 'weight', 'photos', 'description', 'status', 'published_at', 'updated_at', 'shelter_id']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'pet', 'user', 'message']