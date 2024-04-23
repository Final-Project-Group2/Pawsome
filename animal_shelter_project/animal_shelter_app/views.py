from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Pet, Application
from .forms import AddPetForm , ApplicationForm
from urllib.parse import urlparse
from user_managment_app.models import Shelter
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from filters.forms import PetFilterForm


class PetListView(ListView):
    model = Pet
    template_name = 'pet_list.html'
    context_object_name = 'pets'
    
    def get_queryset(self):
        shelter_pk = self.kwargs.get('pk')

        if shelter_pk:
            queryset = Pet.objects.filter(shelter_id=shelter_pk)
        else:
            queryset = Pet.objects.all()
            
        form = PetFilterForm(self.request.GET)
        if form.is_valid():
            species = form.cleaned_data.get('species')
            gender = form.cleaned_data.get('gender')
            size = form.cleaned_data.get('size')

            if species:
                queryset = queryset.filter(species=species)
            if gender:
                queryset = queryset.filter(gender=gender)
            if size:
                queryset = queryset.filter(size=size)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shelter_pk = self.kwargs.get('pk')
        if shelter_pk:
            shelter = Shelter.objects.get(pk=shelter_pk)
            context['shelter'] = shelter
        return context


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
        user = self.request.user

        shelter = user.shelter_set.first()
        
        form.instance.shelter_id = shelter.id
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('animal_shelter_app:pet_list')

class AdoptionCreateView(CreateView):
    template_name = 'adoption_form.html'
    form_class = ApplicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the pet object based on the pet_id from URL kwargs
        pet_id = self.kwargs['pet_id']
        pet = Pet.objects.get(id=pet_id)
        # Pass the pet object to the template context
        context['pet'] = pet
        return context

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