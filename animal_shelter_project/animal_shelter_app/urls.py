from django.urls import path
from .views import PetListCreatView, PetDetailView, ApplicationListCreatView, ApplicationDetailView, AddPetView, AdoptionFormView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'animal_shelter_app'

urlpatterns =[
    path('pets/', PetListCreatView.as_view(), name='pet_list'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('add_pet/', AddPetView.as_view(), name='add_pet'), # added by mohsen
    path('applications/', ApplicationListCreatView.as_view(), name='application_list'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
    path('adoption-form/', AdoptionFormView.as_view(), name='adoption_form'), # added by mohsen

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # added by mohsen