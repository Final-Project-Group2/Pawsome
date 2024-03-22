from rest_framework import serializers
from django.core.validators import validate_email
from .models import CustomUser, Shelter

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 
                  'username', 
                  'password', 
                  'email',
                  'first_name', 
                  'last_name',
                  'street_address',
                  'city',
                  'country',
                  'image')
        
        def validate_email(self, value):
            try:
                validate_email(value)
            except ValueError as e:
                raise serializers.ValidationError(str(e))
            return value
        
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