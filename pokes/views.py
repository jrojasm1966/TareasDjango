from abc import abstractmethod
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Poke
from django.db.models import Count, Q


# Create your views here.
def pokes(request):
    # Identificación de Página para despliegue de Menú navbar
    paginaActual = "pokes"
    
    active_user = User.objects.get(id=request.session['user_id'])
    
    # 2 formas de la misma consulta:
    #cantTotalPokes = Poke.objects.filter(receptor_id = asd).exclude(emisor_id=request.session['user_id']).count()
    #cantTotalPokes = Poke.objects.filter(~ Q (emisor_id=request.session['user_id']), receptor_id = asd).count()
    cantTotalPokes = Poke.objects.filter(receptor_id = active_user).count()

    # Uso de aggregate para saber cuantos pokes recibe el conectado como usuario y receptor_id en Poke
    numPokes = Poke.objects.aggregate(
    numPokesReceptor=Count(
        'emisor_id', 
        filter = Q (receptor_id = active_user),
        distinct=True
    ))
    
    # Query directa con JOIN y Busca al usuario conectado para obtener su historial de pokes recibidos por otros usuarios
    poke_user = Poke.objects.raw(
        "SELECT b.id, b.nombre, b.alias, count(*) as cantpokes FROM pokes_poke a JOIN login_user b ON a.emisor_id = b.id and a.receptor_id = " + str(request.session['user_id']) + " GROUP BY a.emisor_id"
        )

    # Lista de Usuarios a desplegar sus datos con el resumen de pokes recibidos
    lista_usuarios = Poke.objects.raw(
        "SELECT b.id, b.nombre, b.alias, b.email, count(a.receptor_id) as cantpokes FROM pokes_poke a JOIN login_user b ON a.receptor_id = b.id and a.receptor_id not in (" + str(request.session['user_id']) + ") GROUP BY a.receptor_id"
        )

    context = {
        "paginaActual": paginaActual,
        "active_user": active_user,
        "cantTotalPokes": cantTotalPokes,
        "numPokes": numPokes, # Corresponde a aggregate
        "poke_user" : poke_user,
        "lista_usuarios" : lista_usuarios
    }

    return render(request, 'home_pokes.html', context)

def add_poke(request):
    receptor_id = User.objects.get(id=request.POST["id"])
    emisor_id = User.objects.get(id=request.session["user_id"])
    poke = Poke.objects.create(emisor = emisor_id, receptor = receptor_id)
    
    return redirect("/pokes")
    
    