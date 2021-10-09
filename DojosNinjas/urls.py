from django.urls import path

from . import views

urlpatterns = [
    path('admDojosNinjas', views.DojosNinjas, name='DojosNinjas'),
    path('shellDojosNinjas', views.shellDojosNinjas, name='shellDojosNinjas'),
    
    path('admcreateDojos', views.createDojos, name='createDojos'),
    path('admupdateDojos', views.updateDojos, name='updateDojos'),
    path('admgetDojos', views.getDojos, name='getDojos'),
    path('admdeleteDojos', views.deleteDojos, name='deleteDojos'),

    path('admcreateNinjas', views.createNinjas, name='createNinjas'),
    path('admupdateNinjas', views.updateNinjas, name='updateNinjas'),
    path('admgetNinjas', views.getNinjas, name='getNinjas'),
    path('admdeleteNinjas', views.deleteNinjas, name='deleteNinjas'),
    
    path('admcambiarRelacionDojosNinjas', views.cambiarRelacionDojosNinjas, name='cambiarRelacionDojosNinjas'),
    path('admcambiarRelacionDN', views.cambiarRelacionDN, name='cambiarRelacionDN'),

]