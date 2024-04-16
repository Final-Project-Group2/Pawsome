from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import FormView, ListView, TemplateView
from django.utils import timezone
import django_filters
import django_filters.rest_framework as filters
from django.urls import reverse_lazy
from rest_framework import generics
from .models import Pet, Application
from .serializers import PetSerializer, ApplicationSerializer
from .forms import AddPetForm , ApplicationForm
from urllib.parse import urlparse



class PetFilter(django_filters.FilterSet):
    species = filters.CharFilter(field_name='species')
    gender = filters.CharFilter(field_name='gender')
    size = filters.CharFilter(field_name="size")
    status = filters.CharFilter(field_name="status")
    class Meta:
        model = Pet
        fields = ['species', 'gender', 'size', 'status']

class ApplicationFilter(django_filters.FilterSet):
    month = filters.CharFilter(field_name='created_at', lookup_expr='month')
    year = filters.CharFilter(field_name='created_at', lookup_expr='year')
    class Meta:
        model = Application
        fields = ['month', 'year']

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

    


# class PetDetailView(ListView):
#     model = Pet
#     template_name = "pet_detail.html" 
#     context_object_name = "pet"

#     def get_queryset(self):
#         return Pet.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         profile = self.get_queryset().first()
#         context['pet'] = profile
#         return context


class ApplicationListCreatView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ApplicationFilter

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


    

class AddPetView(FormView):# added by mohsen
    model = Pet
    template_name = 'add_pet.html'
    form_class = AddPetForm
    success_url = reverse_lazy('pets_list')

    def form_valid(self, form):
        return super().form_valid(form)



    def get_success_url(self):
        return self.success_url
    

class AdoptionFormView(FormView): # added by mohsen
    template_name = 'adoption_form.html'
    form_class = ApplicationForm
    success_url = '/adopton_thank_you/' 
    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.success_url
    

class ThankYouView(TemplateView):    # added by mohsen
    template_name = 'adoption_thank_you.html'