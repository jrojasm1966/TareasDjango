from django.shortcuts import render, redirect
from .models import *
from login.models import User

def wizard(request):
    paginaActual = "wizard"
    active_user = User.objects.get(id=request.session['user_id'])
    wizards = Wizard.objects.all()
    
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_wizards': wizards,
    }
    return render(request, 'wizardCRUD.html', context)

def createwizard(request):
    # Añadir un registro de tabla:
    Wizard.objects.create(
        name= request.POST['nameWizard'],
        house= request.POST['casaWizard'],
        pet= request.POST['mascotaWizard'],
        year= request.POST['yearWizard']
        )
    return redirect('/admSQLORM')

def getwizard(request):
    paginaActual = "wizard"
    active_user = User.objects.get(id=request.session['user_id'])
    getWizard = Wizard.objects.get(id=request.POST['id'])
    
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getWizard": getWizard
    }
    return render(request,'editWizard.html', context)

def updatewizard(request):
    Wizard.objects.filter(id = request.POST['id']).update(
        name= request.POST['nameWizard'],
        house= request.POST['casaWizard'],
        pet= request.POST['mascotaWizard'],
        year= request.POST['yearWizard']
        )
    return redirect('/admSQLORM')

def deletewizard(request):
    Wizard.objects.get(id = request.POST['id']).delete()
    return redirect('/admSQLORM')

