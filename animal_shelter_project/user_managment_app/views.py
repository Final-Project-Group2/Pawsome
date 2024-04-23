from rest_framework import generics,status
from rest_framework.response import Response
from .models import CustomUser, Shelter
from .serializers import CustomUserSerializer, ShelterSerializer
import django_filters
import django_filters.rest_framework as filters
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.conf import settings
from animal_shelter_app.models import Pet
from animal_shelter_app.serializers import PetSerializer
from django.views.generic import CreateView, View, ListView, TemplateView, DetailView
from .forms import CustomUserForm, ShelterSignUpForm, CustomUserChangeForm, ShelterChangeForm 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import check_password, make_password, get_hasher
from django.contrib.auth import authenticate, login
from .forms import ShelterSignUpForm
from django.db import IntegrityError
from animal_shelter_app.models import Application

class UserFilter(django_filters.FilterSet):
    username = filters.CharFilter(field_name='username')
    first_name = filters.CharFilter(field_name='first_name')
    last_name = filters.CharFilter(field_name='last_name')
    username_sw= filters.CharFilter(field_name='username',lookup_expr='strartswith')
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'username_sw']

class CustomUserListCreatView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filters_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = UserFilter

    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     users = self.serializer_class(queryset, many=True)
    #     return render(request, 'shelter_list.html', {'users': users.data})
    
    
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
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the shelter object
        shelter = self.get_object()
        
        # Get all pets related to the shelter
        pets = Pet.objects.filter(shelter=shelter) 

        context['pets'] = pets
        context['user'] = self.request.user
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
    success_url = reverse_lazy("user_profile")
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
            return redirect('home')  
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

class EditShelterProfileView(View):
    template_name = 'edit_shelter_profile.html'
    success_url = reverse_lazy("shelter_profile")
    
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
            return redirect('home')  
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