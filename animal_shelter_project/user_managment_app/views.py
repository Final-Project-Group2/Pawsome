from rest_framework import generics
from rest_framework.response import Response
from .models import CustomUser, Shelter
from .serializers import CustomUserSerializer
from django.shortcuts import render,redirect
from animal_shelter_app.models import Pet
from django.views.generic import CreateView, View, ListView, TemplateView, DetailView
from .forms import CustomUserForm, ShelterSignUpForm, CustomUserChangeForm, ShelterChangeForm 
from django.urls import reverse_lazy
from .forms import ShelterSignUpForm
from django.db import IntegrityError
from animal_shelter_app.models import Application
from filters.forms import PetFilterForm

    
class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        shelter_users = CustomUser.objects.filter(is_shelter=True)
        normal_users = CustomUser.objects.filter(is_shelter=False)
        
        shelter_serializer = CustomUserSerializer(shelter_users, many=True)
        normal_serializer = CustomUserSerializer(normal_users, many=True)

        return Response({
            'serializer': serializer.data,
            'shelter': shelter_serializer.data,
            'user': normal_serializer.data
        })

class ShelterListCreatView(generics.ListCreateAPIView):
    queryset = Shelter.objects.all()

    def get(self, request, *args, **kwargs):
        shelters = self.get_queryset()
        users = CustomUser.objects.filter(is_shelter=True)  
        return render(request, 'shelter_list.html', {'shelters': shelters, 'users': users})


class ShelterDetailView(DetailView):
    model = Shelter
    template_name = "shelter_detail.html"
    context_object_name = "shelter"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shelter = self.get_object()
        
        # Get all pets related to the shelter
        pets = Pet.objects.filter(shelter=shelter, status__in=['adoptable', 'pending_adoption'])

        # Apply filtering if form is submitted
        form = PetFilterForm(self.request.GET)
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

        context['pets'] = pets
        context['filter_form'] = form  # Pass the form to the template
        return context

    
class SignUpView(TemplateView):
    template_name = "registration/signup.html"

class SignUpCustomUserView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup_customuser.html"

class SignUpShelterView(CreateView):
    form_class = ShelterSignUpForm
    template_name = 'registration/signup_shelter.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('username', 'This username is already taken.')
            return self.form_invalid(form)
          
class EditCustomUserProfileView(View):
    template_name = 'edit_customuser_profile.html'

    def get(self, request):
        user = request.user
        form = CustomUserChangeForm(instance=user)
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        user = request.user
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_managment_app:customuser_profile')  
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

class EditShelterProfileView(View):
    template_name = 'edit_shelter_profile.html'
    
    def get(self, request):
        user = request.user
        form = ShelterChangeForm(instance=user)
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        user = request.user
        form = ShelterChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect ('user_managment_app:shelter_profile')  
        else:
            context = {'form': form}
            return render(request, self.template_name, context)
        
class CustomUserProfileView(ListView):
    model = CustomUser
    template_name = "customuser_profile.html"
    context_object_name = "profile"

    def get_queryset(self):
        return CustomUser.objects.filter(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applications = Application.objects.filter(user=self.request.user)
        profile = self.get_queryset().first()
        context['profile'] = profile
        context['applications'] = applications
        print(applications)

        return context
    

class ShelterProfileView(ListView):
    model = Shelter
    template_name = "shelter_profile.html"
    context_object_name = "profile"

    def get_queryset(self):
        return Shelter.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = context['object_list'].first() 
        context['profile'] = profile

        return context