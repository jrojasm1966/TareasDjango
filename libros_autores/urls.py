from django.urls import path
from . import views

urlpatterns = [
    path('librosautoresSHELL', views.librosautoresSHELL, name='librosautoresSHELL'),
    path('librosAutores', views.librosAutores, name='librosAutores'),
    path('admlibros', views.admlibros, name='admlibros'),
    path('admcreateLibroAutor', views.createLibroAutor, name='createLibroAutor'),
    path('admupdateLibroAutor', views.updateLibroAutor, name='updateLibroAutor'),
    path('admgetLibroAutor', views.getLibroAutor, name='getLibroAutor'),

    path('admautores', views.admautores, name='admautores'),
    path('admcreateAutorLibro', views.createAutorLibro, name='createAutorLibro'),
    path('admupdateAutorLibro', views.updateAutorLibro, name='updateAutorLibro'),
    path('admgetAutorLibro', views.getAutorLibro, name='getAutorLibro'),
]