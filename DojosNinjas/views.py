from time import gmtime, strftime, localtime
from django.db.models.fields import IntegerField
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from login.models import User

# Métodos de Control para Mantención de Dojos y Ninjas
def shellDojosNinjas(request):
    paginaActual = "shellDojosNinjas"
    active_user = User.objects.get(id=request.session['user_id'])

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
    }
    return render(request, 'dojosninjasShell.html', context)

def DojosNinjas(request):
    paginaActual = "DojosNinjas"
    active_user = User.objects.get(id=request.session['user_id'])
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_dojos': dojos,
        'lista_ninjas': ninjas,
    }
    return render(request, 'DojosNinjasMant.html', context)

def createDojos(request):
    # Añadir un registro de tabla:
    Dojos = Dojo(
        nombre= request.POST['nameDojo'],
        ciudad= request.POST['ciudadDojo'],
        estado= request.POST['estadoDojo'],
        created_at = localtime,
        updated_at = localtime
        )
    Dojos.save()
    return redirect('/admDojosNinjas')

def getDojos(request):
    paginaActual = "DojosNinjas"
    active_user = User.objects.get(id=request.session['user_id'])
    getDojo = Dojo.objects.get(id=request.POST['id'])
    
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getDojo": getDojo
    }
    return render(request,'EditDojo.html', context)

def updateDojos(request):
    Dojo.objects.filter(id = request.POST['id']).update(
        nombre= request.POST['nameDojo'],
        ciudad= request.POST['ciudadDojo'],
        estado= request.POST['estadoDojo'],
        updated_at = localtime
        )
    return redirect('/admDojosNinjas')

def deleteDojos(request):
    Dojo.objects.get(id = request.POST['id']).delete()
    return redirect('/admDojosNinjas')

def createNinjas(request):
    # Añadir un registro de tabla:
    ninja = Ninja(
        dojo_id = Dojo.objects.get(id = request.POST['eligeDojo']),
        nombre= request.POST['nameNinja'],
        apellido= request.POST['apeNinja'],
        created_at = localtime,
        updated_at = localtime
    )
    ninja.save()
    return redirect('/admDojosNinjas')

def getNinjas(request):
    paginaActual = "DojosNinjas"
    active_user = User.objects.get(id=request.session['user_id'])
    getNinja = Ninja.objects.get(id=request.POST['id'])
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getNinja": getNinja
    }
    return render(request,'EditNinja.html', context)

def updateNinjas(request):
    Ninja.objects.filter(id = request.POST['id']).update(
        nombre= request.POST['nameNinja'],
        apellido= request.POST['apeNinja'],
        updated_at = localtime
        )
    return redirect('/admDojosNinjas')

def deleteNinjas(request):
    Ninja.objects.get(id = request.POST['id']).delete()
    return redirect('/admDojosNinjas')

def cambiarRelacionDojosNinjas(request):
    paginaActual = "DojosNinjas"
    active_user = User.objects.get(id=request.session['user_id'])
    getNinja = Ninja.objects.get(id=request.POST['id'])
    dojos = Dojo.objects.all()

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getNinja": getNinja,
        'lista_dojos': dojos,
    }
    return render(request, 'CambiarRelacionDojosNinjas.html', context)

def cambiarRelacionDN(request):
    # Elimina relación
    this_ninja = Ninja.objects.get(id = request.POST['id'])	# recupera una instancia de un ninja
    this_dojo = Dojo.objects.get(id = request.POST['idPub'])	# recuperar una instancia de un dojo
        
    # 2 opciones que hacen lo mismo
    this_dojo.dojo_id.remove(this_ninja)		# eliminar el dojo de la lista de libros de este ninja
    # O
    #this_ninja.dojo_id.remove(this_dojo)	# eliminar al ninja de la lista de dojo

    # Agrega relación
    # 2 opciones que hacen lo mismo
    this_dojo.dojo_id.add(this_ninja)		# añadir el dojo a la lista de ninja
    # O
    #this_ninja.dojo_id.add(this_dojo)	# agregar el ninja a la lista de dojo

    return redirect('/admDojosNinjas')
    

