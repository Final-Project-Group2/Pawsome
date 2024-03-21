from rest_framework import generics
from .models import CustomUser, Shelter
from .serializers import CustomUserSerializer, ShelterSerializer
import django_filters
import django_filters.rest_framework as filters

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

class ShelterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer