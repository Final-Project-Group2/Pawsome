from rest_framework import generics
from .models import Pet, Shelter, Application
from .serializers import PetSerializer, ShelterSerializer, ApplicationSerializer
import django_filters
import django_filters.rest_framework as filters

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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PetFilter

class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class ShelterListCreatView(generics.ListCreateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class ShelterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class ApplicationListCreatView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ApplicationFilter

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

