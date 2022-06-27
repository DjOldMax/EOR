from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    books=[i for i in BOOKS.objects.all()]
    context={
        'books':books
    }
    print(context)
    return render(request, 'index.html', context = context)


def show_book(request, book_id):
    context={
        'book_id':str(book_id)
    }
    return render(request, 'book.html', context=context)