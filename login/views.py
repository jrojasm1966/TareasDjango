from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
import bcrypt

from .models import User

# Create your views here.
def login(request):
    return render(request, 'registro.html')

#def registrar(request):
#    return render(request, 'registro.html')

def menu(request):
    active_user = User.objects.get(id=request.session['user_id'])

    context = {
        "active_user": active_user,
    }
    return render(request, 'menuGeneral.html', context)
    #return render(request, 'menuGeneral.html')

def inicio(request):
    usuario = User.objects.filter(email=request.POST['email2'])
    errores = User.objects.validar_login(request.POST, usuario)

    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = usuario[0].id
        return redirect('menu')

def registro(request):
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/registro')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        decode_hash_pw = password.decode('utf-8')
        
        rol = 2
        if User.objects.all().count() == 0:
            rol = 1
            
        #crear usuario
        if request.POST['rol'] == '1':
            user = User.objects.create(
                nombre=request.POST['nombre'],
                alias=request.POST['alias'],
                email=request.POST['email'],
                cumple=request.POST['cumple'],
                password=decode_hash_pw,
                rol=1,
            )
        else:
            user = User.objects.create(
                nombre=request.POST['nombre'],
                alias=request.POST['alias'],
                email=request.POST['email'],
                cumple=request.POST['cumple'],
                password=decode_hash_pw,
                rol=2,
            )
        request.session['user_id'] = user.id
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')