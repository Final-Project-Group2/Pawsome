from rest_framework import generics
from .models import CustomUser, Shelter
from .serializers import CustomUserSerializer, ShelterSerializer
import django_filters
import django_filters.rest_framework as filters
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, ListView, TemplateView
from .forms import CustomUserForm, ShelterSignUpForm, CustomUserChangeForm, ShelterChangeForm 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import check_password, make_password, get_hasher
from django.contrib.auth import authenticate, login
from .forms import ShelterSignUpForm
from django.db import IntegrityError

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

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

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
        profile = self.get_queryset().first()
        context['profile'] = profile
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