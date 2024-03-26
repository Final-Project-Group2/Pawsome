from django.urls import path, include
from .views import Home, Contact, AllPets
from rest_framework.routers import SimpleRouter
from .apiviews import  PetsSet
route = SimpleRouter()
route.register(r"", PetsSet ,basename="pets")
urlpatterns = [
      path('',Home.as_view(),name='home_page'),
      path('contact/',Contact.as_view(),name='contact_page'),
      path('pets/', AllPets.as_view(),name='allpets_page'),

]