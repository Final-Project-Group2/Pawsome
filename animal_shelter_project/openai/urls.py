from django.urls import path
from .views import *

app_name = "openai"

urlpatterns =[
    path('adoption_preference/', adoption_preference_form_view, name='asoption_preference'),
]
