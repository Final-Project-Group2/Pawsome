from django.shortcuts import render,get_object_or_404
from django.views.generic import FormView, CreateView, TemplateView, UpdateView, DetailView
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