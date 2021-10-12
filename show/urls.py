from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.show),
    path('shows/new', views.addShow),
    path('shows/showAdd', views.showAdd),
    path('shows/<int:id>/', views.TvShow),
    path('shows/<int:id>/edit', views.EditShow),
    path('shows/<int:id>/update', views.UpdateShow),
    path('shows/<int:id>/destroy', views.DeleteShow),
]