from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('admTablas', views.polls, name='polls'),
    path('admclientes', views.clientes, name='clientes'),
    path('admsitios', views.sitios, name='sitios'),
    path('admleads', views.leads, name='leads'),
    path('admdocs', views.docs, name='docs'),
    path('admlibrosPublicadores', views.librosPublicadores, name='librosPublicadores'),
    
    path('admcreatePub', views.createPub, name='createPub'),
    path('admupdatePub', views.updatePub, name='updatePub'),
    path('admgetPub', views.getPub, name='getPub'),
    path('admdeletePub', views.deletePub, name='deletePub'),

    path('admcreateLibro', views.createLibro, name='createLibro'),
    path('admupdateLibro', views.updateLibro, name='updateLibro'),
    path('admgetLibro', views.getLibro, name='getLibro'),
    path('admdeleteLibro', views.deleteLibro, name='deleteLibro'),
    path('admagregaRelacionLibroEditor', views.agregaRelacionLibroEditor, name='agregaRelacionLibroEditor'),
    path('admagregaRelacion', views.agregaRelacion, name='agregaRelacion'),
    path('admdeleteRelacionLibroEditor', views.deleteRelacionLibroEditor, name='deleteRelacionLibroEditor'),
    path('admdeleteRelacion', views.deleteRelacion, name='deleteRelacion'),

]