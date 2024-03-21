from django.urls import path
from .views import CustomUserListCreatView, CustomUserDetailView, ShelterListCreatView, ShelterDetailView

name_app = "user_managment_app"

urlpatterns =[
    path('shelters/', ShelterListCreatView.as_view(), name='shelter_list'),
    path('shelter/<int:pk>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('users/', CustomUserListCreatView.as_view(), name='user_list'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
]