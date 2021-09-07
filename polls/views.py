#from djangoAdmin.polls.models import Client
#from _typeshed import SupportsItems
from polls.models import Client
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

#def index(request):
    #return render(request, 'polls/index.html')
    
def home(request):
    return render(request, 'polls/home.html')


def clientes(request):
    clientes = Client.objects.all()
    context = {
        'lista_clientes': clientes,
    }
    return render(request, 'polls/cliente.html', context)


def sitios(request):
    sitios = Site.objects.all()
    context = {
        'lista_sitios': sitios,
    }
    return render(request, 'polls/sitios.html', context)

def leads(request):
    leads = Lead.objects.all()
    context = {
        'lista_leads': leads,
    }
    return render(request, 'polls/leads.html', context)

def docs(request):
    docs = Documento.objects.all()
    context = {
        'lista_docs': docs,
    }
    return render(request, 'polls/docs.html', context)

def librosPublicadores(request):
    libros = Book.objects.all()
    publicadores = Publisher.objects.all()
    context = {
        'lista_libros': libros,
        'lista_publicadores': publicadores,
    }
    return render(request, 'polls/LibroPublicador.html', context)


def librosPublicadoresMant(request):
    libros = Book.objects.all()
    publicadores = Publisher.objects.all()
    context = {
        'lista_libros': libros,
        'lista_publicadores': publicadores,
    }
    return render(request, 'polls/LibroPublicadorMant.html', context)


def createLibro(request):
    Book.objects.create(
    titulo = request.POST['titulo'],
    )
    return redirect('/librosPublicadoresMant')


def getLibro(request):
    getBook = Book.objects.get(id=request.POST['id'])
    context = {
        "getBook": getBook
    }
    return render(request,'polls/EditlibroPublicador.html', context)


def updateLibro(request):
    getBook = Book.objects.get(id=request.POST['id'])
    #Book.title = request.POST['titulo']
    #update()

    Book.objects.update(
    #id = request.POST['id'],
    title = request.POST['titulo'],
    )
    
    return redirect('/librosPublicadoresMant')


def deleteLibro(request):
    getBook = Book.objects.get(id=request.POST['id']).delete()
    return redirect('/librosPublicadoresMant')
