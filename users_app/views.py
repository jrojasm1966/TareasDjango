from django.shortcuts import render, redirect
from .models import *
from login.models import User

# Create your views here.

def usersSHELL(request):
    paginaActual = "usersSHELL"
    active_user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
    }
    return render(request, 'usersSHELL.html', context)
