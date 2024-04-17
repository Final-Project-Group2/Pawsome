from django.shortcuts import render,get_object_or_404
from django.views.generic import FormView, CreateView, TemplateView, UpdateView, DetailView
from django.urls import reverse_lazy
from rest_framework import generics
from .models import Pet, Application
from .serializers import PetSerializer
from .forms import AddPetForm , ApplicationForm
from urllib.parse import urlparse
from user_managment_app.models import Shelter
from django.contrib.auth.mixins import LoginRequiredMixin
from filters.forms import PetFilterForm
from rest_framework.response import Response


class PetListCreatView(generics.ListCreateAPIView):  # added by mohsen
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        species = self.request.query_params.get('species')
        if species:
            queryset = queryset.filter(species=species)
        return queryset
    
    def get(self, request, *args, **kwargs):
        pets = self.get_queryset()
        form = PetFilterForm(request.GET)

        if form.is_valid():
            species = form.cleaned_data.get('species')
            gender = form.cleaned_data.get('gender')
            size = form.cleaned_data.get('size')

            if species:
                pets = pets.filter(species=species)
            if gender:
                pets = pets.filter(gender=gender)
            if size:
                pets = pets.filter(size=size)
        
        return render(request, 'pet_list.html', {'pets': pets, 'form': form})
    
    
# class PetListCreatView(generics.ListCreateAPIView):
#     queryset = Pet.objects.all()
#     serializer_class = PetSerializer
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         species = self.request.query_params.get('species', None)
#         if species:
#             queryset = queryset.filter(species=species)
#         return queryset
    
#     def get(self, request, *args, **kwargs): # added by mohsen
#         pets= self.get_queryset()
#         return render(request, 'pet_list.html', {'pets': pets})


class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        shelter = None


        if user.is_authenticated and user.is_shelter:
            try:
                shelter = Shelter.objects.get(user=user)
            except Shelter.DoesNotExist:
                pass 

        context['shelter'] = shelter
        return context



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

class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'edit_pet_profile.html'
    fields = ['name', 'species', 'breeds', 'age', 'gender', 'size', 'weight', 'photos', 'description']

    def get_success_url(self):
        return reverse_lazy('animal_shelter_app:pet_detail', kwargs={'pk': self.object.pk})