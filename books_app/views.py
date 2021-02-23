from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
# def root(request):
#     return HttpResponse("Hello World!")
# --------------------------------------------


def index(request):
    print(Book.objects.all())
    context = {
        'allbooks': Book.objects.all()
    }
    return render(request, "index.html", context)


def createbook(request):
    print(request.POST['title'])
    print("******")
    print(request.POST['description'])
    print("******")
    Book.objects.create(
        title=request.POST['title'], desc=request.POST['description'],)
    return redirect('/')


def books(request, bookid):
    context = {
        'onebook': Book.objects.get(id=bookid),
        'allAuthors': Author.objects.all()
    }
    print(Book.objects.get(id=bookid))
    return render(request, "index2.html", context)


def addAuthortoBook(request, bookid):
    this_book = Book.objects.get(id=bookid)
    this_author = Author.objects.get(id=request.POST['addAuthor'])
    this_author.notes.add(this_book)
    return redirect(f'/books/{bookid}')
