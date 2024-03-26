from django.shortcuts import render
from rest_framework.reverse import reverse
from django.http import HttpRequest,HttpResponse
from django.views.generic.base import TemplateView 
from django.views.generic import ListView
from rest_framework.decorators import action, permission_classes
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from django.contrib import messages
from rest_framework import status
from .more_settings import us, URLS
from .forms import PetForm, CustomerUserForm
from .serializers import CustomerUserSerializer, PetSerializer,Pet
from requests import request as req

class Home(TemplateView):
      template_name='home.html'
      serializer_class = PetSerializer
      permission_classes = (AllowAny,)

      def get(self, request, *args, **kwargs):
            context = {"us":us}
            pets=None
            if len(Pet.objects.all()) > 0:
                  dogs=Pet.objects.filter(species="dog")
                  cats =Pet.objects.filter(species="cat")
                  pets_l= [ *dogs, *cats]
                  pets=self.serializer_class(pets_l,many=True)
            context["pets"] = pets
            return render(request,self.template_name, context)
      
class Contact(TemplateView):
      template_name='contact.html'
      permission_classes = (AllowAny,)

      def get(self, request, *args, **kwargs):
            context = {"us":us}
            return render(request,self.template_name, context)
      
class AllPets(TemplateView):
      template_name='allpets.html'
      permission_classes = (AllowAny,)

      def get(self, request, *arg, **kwargs):
            url = "https://localhost/api/allpets/"
            pets=req("GET",url=url)
            p=pets.json()
            context={"pets":p}
            return render(request, self.template_name,context)

