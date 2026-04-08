from django.urls import path
from login import views

urlpatterns = [
    path('add_user/', views.add_user),
    path('users/', views.users),
    path('add_role/', views.add_role),
]
