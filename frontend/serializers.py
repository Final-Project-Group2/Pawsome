from rest_framework import serializers
from .models import CustomerUser, Pet
from django.contrib.auth import get_user_model

class CustomerUserSerializer(serializers.ModelSerializer):
      class Meta:
            model= CustomerUser
            fields = "__all__"


class PetSerializer(serializers.ModelSerializer):
      class Meta:
            model= Pet
            fields = "__all__"