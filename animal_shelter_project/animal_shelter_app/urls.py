from django.urls import path
from .views import PetListCreatView, PetDetailView, ApplicationListCreatView, ApplicationDetailView

name_app = "animal_shelter_app"

urlpatterns =[
    path('pets/', PetListCreatView.as_view(), name='pet_list'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('applications/', ApplicationListCreatView.as_view(), name='application_list'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
]