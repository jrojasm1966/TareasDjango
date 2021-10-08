from django.urls import path
from . import views

urlpatterns = [
    path('admSQLORM', views.wizard, name='wizard'),

    path('admcreateWizard', views.createwizard, name='createwizard'),
    path('admupdateWizard', views.updatewizard, name='updatewizard'),
    path('admgetWizard', views.getwizard, name='getwizard'),
    path('admdeleteWizard', views.deletewizard, name='deletewizard'),

]