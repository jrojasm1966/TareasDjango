from django.shortcuts import render, redirect
from .models import *
from login.models import User
from time import localtime

# Create your views here.

def librosautoresSHELL(request):
    paginaActual = "librosautoresSHELL"
    active_user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
    }
    return render(request, 'librosautoresSHELL.html', context)

def librosAutores(request):
    paginaActual = "librosAutores"
    active_user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
    }
    return render(request, 'homeLibrosAutores.html', context)

def admlibros(request):
    paginaActual = "librosAutores"
    active_user = User.objects.get(id=request.session['user_id'])
    libros = books.objects.all()

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_libros': libros,
    }
    return render(request, 'librosMant.html', context)

def createLibroAutor(request):
    # Añadir un registro de tabla:
    libro = books(
        title= request.POST['librotitulo'],
        desc= request.POST['librodesc'],
        created_at = localtime,
        updated_at = localtime)
    libro.save()
    return redirect('/admlibros')


def getLibroAutor(request):
    paginaActual = "librosAutores"
    active_user = User.objects.get(id=request.session['user_id'])
    getBook = books.objects.get(id=request.POST['id'])
    getBookAutor = books_authors.objects.filter(book_id=request.POST['id'])
    getAutor = authors.objects.all()
    #getAutorDisp = books_authors.objects.order_by("author_id").distinct().exclude(book_id=request.POST['id'])

    # Query directa 
    getAutorDisp = books_authors.objects.raw(
        "SELECT a.book_id, a.author_id, b.id FROM libros_autores_books_authors a, libros_autores_authors b where a.author_id = b.id and a.book_id not in (" + str(request.POST['id']) + ") group BY a.author_id")

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getBook": getBook,
        "getBookAutor": getBookAutor,
        "getAutor": getAutor,
        "getAutorDisp": getAutorDisp,
    }
    return render(request,'editLibro.html', context)


def updateLibroAutor(request):
    getBookAutorCount = books_authors.objects.filter(book_id=request.POST['id'],author_id = request.POST['idAutor']).count()
    if getBookAutorCount == 0:
        books_authors.objects.create(
            book_id = request.POST['id'],
            author_id = request.POST['idAutor'])
    return redirect('/admlibros')


def admautores(request):
    paginaActual = "librosAutores"
    active_user = User.objects.get(id=request.session['user_id'])
    autores = authors.objects.all()

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        'lista_autores': autores,
    }
    return render(request, 'autoresMant.html', context)

def createAutorLibro(request):
    # Añadir un registro de tabla:
    libro = authors(
        first_name = request.POST['nombreAutor'],
        last_name = request.POST['apeAutor'],
        notas = request.POST['notasAutor'],
        created_at = localtime,
        updated_at = localtime)
    libro.save()
    return redirect('/admautores')


def getAutorLibro(request):
    paginaActual = "librosAutores"
    active_user = User.objects.get(id=request.session['user_id'])
    getAutor = authors.objects.get(id=request.POST['id'])
    getBookAutor = books_authors.objects.filter(author_id=request.POST['id'])
    getBook = books.objects.all()

    # Query directa 
    getBookDisp = books_authors.objects.raw(
        "SELECT a.book_id, a.author_id, b.id FROM libros_autores_books_authors a, libros_autores_books b where a.book_id = b.id and a.author_id not in (" + str(request.POST['id']) + ") group BY a.book_id")

    context = {
        'paginaActual': paginaActual,
        "active_user": active_user,
        "getAutor": getAutor,
        "getBookAutor": getBookAutor,
        "getBook": getBook,
        "getBookDisp": getBookDisp,
    }
    return render(request,'editAutor.html', context)


def updateAutorLibro(request):
    getAutorBookCount = books_authors.objects.filter(book_id=request.POST['idLibro'],author_id = request.POST['id']).count()
    if getAutorBookCount == 0:
        books_authors.objects.create(
            book_id = request.POST['idLibro'],
            author_id = request.POST['id'])
    return redirect('/admautores')
