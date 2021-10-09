from django.urls import path
from . import views

urlpatterns = [
    path('usersSHELL', views.usersSHELL, name='usersSHELL'),
]