#from djangoAdmin.polls.models import Client
#from _typeshed import SupportsItems
from time import gmtime, strftime, localtime
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
    #publicadores_libros = Publisher_Books.objects.all()
    context = {
        'lista_libros': libros,
        'lista_publicadores': publicadores,
    #    'publicadores_libros': publicadores_libros,
    }
    return render(request, 'polls/LibroPublicadorMant.html', context)


def createLibro(request):
    # Forma 1 de Añadir un registro de tabla:
    #Book.objects.create(title = request.POST['librotitulo'],created_at = localtime,updated_at = localtime)
    
    # Otra forma de Añadir un registro de tabla:
    libro = Book(title= request.POST['librotitulo'],created_at = localtime,updated_at = localtime)
    libro.save()
    return redirect('/librosPublicadoresMant')


def getLibro(request):
    getBook = Book.objects.get(id=request.POST['id'])
    context = {
        "getBook": getBook
    }
    return render(request,'polls/EditlibroPublicador.html', context)


def updateLibro(request):
    Book.objects.filter(id = request.POST['id']).update(title = request.POST['titulo'])
    return redirect('/librosPublicadoresMant')


def deleteLibro(request):
    Book.objects.get(id = request.POST['id']).delete()
    return redirect('/librosPublicadoresMant')

def deleteRelacionLibroEditor(request):
    getBook = Book.objects.get(id=request.POST['id'])
    context = {
        "getBook": getBook,
    }
    return render(request, 'polls/DeleteRelacionBookPub.html', context)


def deleteRelacion(request):
    this_book = Book.objects.get(id = request.POST['idLibro'])	# recupera una instancia de un libro
    this_publisher = Publisher.objects.get(id = request.POST['idPub'])	# recuperar una instancia de un editor
        
    # 2 opciones que hacen lo mismo
    this_publisher.books.remove(this_book)		# eliminar el libro de la lista de libros de este editor
    # O
    #this_book.publishers.remove(this_publisher)	# eliminar al editor de la lista de editores de este libro

    return redirect('/deleteRelacionLibroEditor')
