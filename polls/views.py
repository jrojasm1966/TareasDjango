#from djangoAdmin.polls.models import Client
#from _typeshed import SupportsItems
from time import gmtime, strftime, localtime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from login.models import User

#def index(request):
    #return render(request, 'polls/index.html')

def polls(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
    }
    return render(request, 'polls/home.html', context)
    #return render(request, 'polls/home.html')

def home(request):
    return render(request, 'polls/home.html')

def clientes(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    clientes = Client.objects.all()
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_clientes': clientes,
    }
    return render(request, 'polls/cliente.html', context)

def sitios(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    sitios = Site.objects.all()
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_sitios': sitios,
    }
    return render(request, 'polls/sitios.html', context)

def leads(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    leads = Lead.objects.all()
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_leads': leads,
    }
    return render(request, 'polls/leads.html', context)

def docs(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    docs = Documento.objects.all()
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_docs': docs,
    }
    return render(request, 'polls/docs.html', context)

# Métodos de Control para Mantención de Publicadores y Libros
def librosPublicadores(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    libros = Book.objects.all()
    publicadores = Publisher.objects.all()
    #publicadores_libros = Publisher_Books.objects.all()
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_libros': libros,
        'lista_publicadores': publicadores,
    #    'publicadores_libros': publicadores_libros,
    }
    return render(request, 'polls/LibroPublicadorMant.html', context)

def createPub(request):
    # Añadir un registro de tabla:
    Pub = Publisher(name= request.POST['namePub'],created_at = localtime,updated_at = localtime)
    Pub.save()
    return redirect('/admlibrosPublicadores')

def getPub(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    getPublisher = Publisher.objects.get(id=request.POST['id'])
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getPublisher": getPublisher
    }
    return render(request,'polls/EditPublicador.html', context)

def updatePub(request):
    Publisher.objects.filter(id = request.POST['id']).update(name = request.POST['namePub'])
    return redirect('/admlibrosPublicadores')

def deletePub(request):
    Publisher.objects.get(id = request.POST['id']).delete()
    return redirect('/admlibrosPublicadores')

def createLibro(request):
    # Añadir un registro de tabla:
    libro = Book(title= request.POST['librotitulo'],created_at = localtime,updated_at = localtime)
    libro.save()
    return redirect('/admlibrosPublicadores')

def getLibro(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    getBook = Book.objects.get(id=request.POST['id'])
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getBook": getBook
    }
    return render(request,'polls/Editlibro.html', context)

def updateLibro(request):
    Book.objects.filter(id = request.POST['id']).update(title = request.POST['titulo'])
    return redirect('/admlibrosPublicadores')

def deleteLibro(request):
    Book.objects.get(id = request.POST['id']).delete()
    return redirect('/admlibrosPublicadores')

def agregaRelacionLibroEditor(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    getBook = Book.objects.get(id=request.POST['id'])
    publicadores = Publisher.objects.all()

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getBook": getBook,
        'lista_publicadores': publicadores,
    }
    return render(request, 'polls/AgregaRelacionBookPub.html', context)

def agregaRelacion(request):
    this_book = Book.objects.get(id = request.POST['id'])	# recupera una instancia de un libro
    this_publisher = Publisher.objects.get(id = request.POST['idPub'])	# recuperar una instancia de un editor
        
    # 2 opciones que hacen lo mismo
    this_publisher.books.add(this_book)		# añadir el libro a la lista de libros de esta editorial
    # O
    #this_book.publishers.add(this_publisher)	# agregar el editor a la lista de editores de este libro

    return redirect('/admlibrosPublicadores')

def deleteRelacionLibroEditor(request):
    paginaActual = "polls"
    active_user = User.objects.get(id=request.session['user_id'])
    getBook = Book.objects.get(id=request.POST['id'])
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getBook": getBook,
    }
    return render(request, 'polls/DeleteRelacionBookPub.html', context)

def deleteRelacion(request):
    this_book = Book.objects.get(id = request.POST['id'])	# recupera una instancia de un libro
    this_publisher = Publisher.objects.get(id = request.POST['idPub'])	# recuperar una instancia de un editor
        
    # 2 opciones que hacen lo mismo
    this_publisher.books.remove(this_book)		# eliminar el libro de la lista de libros de este editor
    # O
    #this_book.publishers.remove(this_publisher)	# eliminar al editor de la lista de editores de este libro

    return redirect('/admlibrosPublicadores')
