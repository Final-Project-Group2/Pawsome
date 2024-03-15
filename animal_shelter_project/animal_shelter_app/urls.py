from django.urls import path
from .views import PetListCreatView, PetDetailView, ShelterListCreatView, ShelterDetailView, ApplicationListCreatView, ApplicationDetailView

urlpatterns =[
    path('pets/', PetListCreatView.as_view(), name='pet_list'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('shelters/', ShelterListCreatView.as_view(), name='shelter_list'),
    path('shelter/<int:pk>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('applications/', ApplicationListCreatView.as_view(), name='application_list'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
]