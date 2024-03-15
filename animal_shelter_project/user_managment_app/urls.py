from django.urls import path
from .views import CustomUserListCreatView, CustomUserDetailView

urlpatterns =[
    path('users/', CustomUserListCreatView.as_view(), name='user_list'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
]