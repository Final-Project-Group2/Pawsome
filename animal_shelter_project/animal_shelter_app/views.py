from rest_framework import generics
from .models import Pet, Shelter
from .serializers import PetSerializer, ShelterSerializer, ApplicationSerializer

# Create your views here.
class PetListCreatView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

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



        