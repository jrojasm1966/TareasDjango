from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('menuGeneral', views.menu, name='menu'),
    #path('registrar', views.registrar, name='registrar'),
    path('inicio', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('logout', views.logout, name='logout'),
]