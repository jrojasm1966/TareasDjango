from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home),
    path('home', views.home, name='home'),
    path('clientes', views.clientes, name='clientes'),
    path('sitios', views.sitios, name='sitios'),
    path('leads', views.leads, name='leads'),
    path('docs', views.docs, name='docs'),
    path('librosPublicadores', views.librosPublicadores, name='librosPublicadores'),
]