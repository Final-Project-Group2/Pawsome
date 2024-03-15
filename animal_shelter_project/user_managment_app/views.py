from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create your views here.
class CustomUserListCreatView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer