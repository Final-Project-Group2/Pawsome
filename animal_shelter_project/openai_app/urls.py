from django.urls import path
from .views import *

app_name = "openai_app"

urlpatterns =[
    path('adoption_preference/', AdoptionPreferenceFormView.as_view(), name='adoption_preference'),
]
