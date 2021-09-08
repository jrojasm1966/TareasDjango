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
    path('librosPublicadoresMant', views.librosPublicadoresMant, name='librosPublicadoresMant'),
    
    path('createLibro', views.createLibro),
    path('updateLibro', views.updateLibro, name='updateLibro'),
    path('getLibro', views.getLibro, name='getLibro'),
    path('deleteLibro', views.deleteLibro),
    path('agregaRelacionLibroEditor', views.agregaRelacionLibroEditor),
    path('agregaRelacion', views.agregaRelacion),
    path('deleteRelacionLibroEditor', views.deleteRelacionLibroEditor),
    path('deleteRelacion', views.deleteRelacion),

]