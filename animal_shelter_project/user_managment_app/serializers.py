from rest_framework import serializers
from django.core.validators import validate_email
from .models import CustomUser

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