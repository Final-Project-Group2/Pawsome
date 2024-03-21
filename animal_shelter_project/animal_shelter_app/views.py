from django.shortcuts import render
import django_filters
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet, Shelter
from .serializers import PetSerializer, ShelterSerializer, ApplicationSerializer
from django.urls import reverse




 # Create your views here.
class PetListCreatView(generics.ListCreateAPIView):
     queryset = Pet.objects.all()
     serializer_class = PetSerializer

class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Pet.objects.all()
     serializer_class = PetSerializer

class ShelterListCreatView(generics.ListCreateAPIView):
     queryset = Shelter.objects.all()
     serializer_class = ShelterSerializer
     
     def get(self, request, *args, **kwargs):# added by mohsen
        #url = reverse('animal_shelter_app:shelter_detail', args=['pk'])
        shelters = self.get_queryset()
        return render(request, 'shelter_list.html', {'shelters': shelters })  #, 'url' : url})
    

class ShelterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    
    def get(self, request, *args, **kwargs):# added by mohsen
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return render(request, 'shelter_detail.html', {'serializer': serializer.data})


class ApplicationListCreatView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ApplicationFilter

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer



        