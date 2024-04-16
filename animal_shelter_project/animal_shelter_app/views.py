from django.shortcuts import render,get_object_or_404
from django.views.generic import FormView, CreateView, TemplateView
from django.urls import reverse_lazy
from rest_framework import generics
from .models import Pet, Application
from .serializers import PetSerializer
from .forms import AddPetForm , ApplicationForm
from urllib.parse import urlparse
from user_managment_app.models import Shelter
from django.contrib.auth.mixins import LoginRequiredMixin

class PetListCreatView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        species = self.request.query_params.get('species', None)
        if species:
            queryset = queryset.filter(species=species)
        return queryset
    
    def get(self, request, *args, **kwargs): # added by mohsen
        pets= self.get_queryset()
        return render(request, 'pet_list.html', {'pets': pets})


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Pet.objects.all()
     serializer_class = PetSerializer
     
     def get(self, request, *args, **kwargs):# added by mohsen
        instance = self.get_object()
        pet = self.get_serializer(instance)
        relative_path = urlparse(pet.data['photos']).path
        shelter_name = instance.shelter.shelter_name if instance.shelter else None

        return render(request, 'pet_detail.html', {'pet': pet.data , 'pet_photo_path': relative_path , 'shelter_name': shelter_name})


class AddPetView(LoginRequiredMixin, CreateView):
    template_name = 'add_pet.html'
    form_class = AddPetForm
    model = Pet

    def form_valid(self, form):
        # Retrieve the current user
        user = self.request.user
        
        # Retrieve the shelter associated with the user
        shelter = user.shelter_set.first()
        
        # Set the shelter_id on the form instance
        form.instance.shelter_id = shelter.id
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('animal_shelter_app:pet_list')

class AdoptionCreateView(CreateView):
    template_name = 'adoption_form.html'
    form_class = ApplicationForm

    def form_valid(self, form):
        pet_id = self.kwargs['pet_id']
        pet = Pet.objects.get(id=pet_id)
        form.instance.pet = pet
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('animal_shelter_app:adoption_success')

class AdoptionSuccessView(TemplateView):
    template_name = 'adoption_success.html'