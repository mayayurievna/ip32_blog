from django.urls import path
from login import views

urlpatterns = [
    path('', views.index),
    path('add_user/', views.add_user),
    path('users/', views.users),
    path('add_role/', views.add_role),
    path('login/', views.login),
    path('logout', views.logout_view),
]
