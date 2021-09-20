from django.urls import path, include
from . import views

urlpatterns = [                  
    path('pokes', views.pokes, name='pokes'),
    path('addpoke', views.add_poke, name='add_poke'),
]