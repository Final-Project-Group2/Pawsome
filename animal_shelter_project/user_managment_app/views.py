from rest_framework import generics
from .models import CustomUser, Shelter
from .serializers import CustomUserSerializer, ShelterSerializer
import django_filters
import django_filters.rest_framework as filters
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from animal_shelter_app.models import Pet
from animal_shelter_app.serializers import PetSerializer

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

# class ShelterDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Shelter.objects.all()
#     serializer_class = ShelterSerializer

#     def get(self, request, *args, **kwargs):# added by mohsen
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return render(request, 'shelter_detail.html', {'serializer': serializer.data})
    


class ShelterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Retrieve pets in this shelter
        dogs = Pet.objects.filter(shelter=instance, species='dog')
        cats = Pet.objects.filter(shelter=instance, species='cat')
    

        return render(request, 'shelter_detail.html', {'serializer': serializer.data, 'dogs': dogs, 'cats': cats, })
